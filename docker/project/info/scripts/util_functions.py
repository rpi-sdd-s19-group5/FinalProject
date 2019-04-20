from datetime import timedelta

from django.utils import timezone
from gsearch.googlesearch import search

from info.models import RelatedPages, CourseInfo, ArchivedPages


def search_related_links(course_info):
    """

    :rtype: list[RelatedPages]
    :type course_info: CourseInfo
    """
    seven_days_ago = timezone.now() - timedelta(days=7)
    related_links = RelatedPages.objects.filter(course=course_info, updated_time__gte=seven_days_ago).order_by('id')

    # if database doesn't have enough related_links or (some of the) links are outdated
    if related_links.count() != 5:
        print('link expired?')
        title = course_info.course_code + " " + course_info.title
        results = search(title)[0:5]
        for item in results:
            print(item[0])
        related_links2 = RelatedPages.objects.filter(course=course_info).order_by('updated_at')

        # if database doesn't have enough related_links (including outdated ones)
        if related_links2.count() != 5:
            # save all results into database
            for url in results:
                RelatedPages(title=url[0], links=url[1], course=course_info, updated_time=timezone.now()).save()

        else:
            print('link expired.')
            # update all info into database
            for RelatedPage, url in zip(related_links2, results):
                # if any entry is updated, put the old entry into archive table, and save the new one
                print(RelatedPage.title)
                print(url[0])
                #if (RelatedPage.title != url[0]) or (RelatedPage.links != url[1]):
                print('updating archive')
                # delete oldest archived link
                if (len(ArchivedPages.objects.all()) == 5) and RelatedPage.updated_time < seven_days_ago :
                    (ArchivedPages.objects.filter(course=course_info).order_by('updated_at'))[0].delete()
                    # put new entry into archive
                if RelatedPage.updated_time < seven_days_ago:
                    ArchivedPages.objects.update_or_create(links=RelatedPage.links, title=RelatedPage.title, course=RelatedPage.course, updated_time=RelatedPage.updated_time)
                    # update list of existing latest links
                    RelatedPage.title = url[0]
                    RelatedPage.links = url[1]
                    RelatedPage.save()



        # Update links lists
        related_links = RelatedPages.objects.filter(course=course_info, updated_at__gte=seven_days_ago).order_by('id')

    return related_links

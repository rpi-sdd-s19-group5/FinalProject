from datetime import timedelta

from django.utils import timezone
from gsearch.googlesearch import search

from info.models import RelatedPages, CourseInfo


def search_related_links(course_info):
    """

    :rtype: list[RelatedPages]
    :type course_info: CourseInfo
    """
    seven_days_ago = timezone.now() - timedelta(days=7)
    related_links = RelatedPages.objects.filter(course=course_info, updated_at__gte=seven_days_ago).order_by('id')

    # if database doesn't have related_links or links is outdated
    if related_links.count() != 5:
        title = course_info.course_code + " " + course_info.title
        results = search(title)[0:5]
        related_links = RelatedPages.objects.filter(course=course_info)

        # if database doesn't have related_links
        if related_links.count() != 5:
            # save all info into database
            for url in results:
                RelatedPages(title=url[0], links=url[1], course=course_info).save()

        else:
            # update all info into database
            for RelatedPage, url in zip(related_links, results):
                RelatedPage.title = url[0]
                RelatedPage.links = url[1]
                RelatedPage.save()

        # Update links lists
        related_links = RelatedPages.objects.filter(course=course_info, updated_at__gte=seven_days_ago).order_by('id')

    return related_links

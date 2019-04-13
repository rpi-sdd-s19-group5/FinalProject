from django.http import Http404
from django.shortcuts import render

from info.models import CourseInfo, ProfAndCourses
from info.models import ProfInfo
from info.scripts.util_functions import search_related_links


def index(request):
    return render(request, 'polls/main.html')


def index_prof(request):
    return render(request, 'polls/main_faculty.html')


# List the search results from required parameter
def search_course2(request):
    if request.GET:
        print(request.GET)
        dept = request.GET["dept"].split(":")[1]
        # 1 = alphabetical; 2 = course code; 3 = relevance
        sort_option = request.GET["sort"]
        dept = ("ALL" if dept == "All Departments" else dept)
        search_content = request.GET["search_content"]
        course_result2 = CourseInfo.search_course_tool(search_content, dept, sort_option)[:10]

        context = {
            'search_results': course_result2,
            'dept': dept,
            'search_content': search_content,
            'sort_value': sort_option,
        }
    else:
        course_result2 = CourseInfo.objects.all()[:10]
        context = {
            'search_results': course_result2,
        }

    # print(course_result2)
    return render(request, 'polls/search_course.html', context)


def search_course(request):
    if request.GET:
        # print(request.GET)
        dept = request.GET["dept"].split(":")[1]
        # 1 = alphabetical; 2 = course code; 3 = relevance
        # sort_option = request.GET["sort"]
        dept = ("ALL" if dept == "All Departments" else dept)
        search_content = request.GET["search_content"]
        course_result = CourseInfo.search_course_tool(search_content, dept, 2)[:10]
        # course_result = []
        context = {
            'search_results': course_result,
            'dept': dept,
            'search_content': search_content,
        }
    else:
        course_result = CourseInfo.objects.all()[:10]
        context = {
            'search_results': course_result,
        }

    # print(course_result)
    return render(request, 'polls/search_course.html', context)


# List the detail information of course
def course_detail(request, name_num):
    course = CourseInfo.objects.filter(course_code=name_num)
    if len(course) == 1:
        related_links = search_related_links(course[0])
        context = {'course_info': course[0],
                   'related_links': related_links}
        return render(request, 'polls/course.html', context)
    else:
        return Http404('Course not found')


# List all related professors
def search_prof(request):
    if request.GET:
        print(request.GET)
        search_content = request.GET["search_content"]
        print(search_content)
        prof_result = ProfInfo.search_prof_tool(search_content)[:10]

        for prof in prof_result: prof["dept"] = prof["dept"].replace('|', ' ')
        context = {
            'search_results': prof_result,
            'search_content': search_content,
        }
    else:
        prof_result = ProfInfo.objects.all()[:10]
        for prof in prof_result: prof.dept = prof.dept.replace('|', ' ')
        context = {
            'search_results': prof_result,
        }

    return render(request, 'polls/search_faculty.html', context)


# Get professor home page
def prof_detail(request, name, db_id):
    result = ProfInfo.objects.filter(id=db_id)
    if len(result) == 1:
        prof = result[0]
    else:
        return Http404('Prof not found')
    courses = ProfAndCourses.search_test(name)
    context = {'prof_info': prof, 'prof_course': courses}
    return render(request, 'polls/faculty.html', context)

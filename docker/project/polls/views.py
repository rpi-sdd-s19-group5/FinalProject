from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

from info.models import CourseInfo, ProfAndCourses
from info.models import ProfInfo
from info.scripts.util_functions import search_related_links


def index(request):
    return render(request, 'polls/main.html')


def index_prof(request):
    return render(request, 'polls/main_faculty.html')


# List the search results from required parameter
def search_course(request):
    if request.GET and "search_content" in request.GET:
        # print(request.GET)
        dept = request.GET["dept"].split(":")[1]
        # 1 = alphabetical; 2 = course code; 3 = relevance
        if "sort" in request.GET:
            sort_option = request.GET["sort"]
        else:
            sort_option = 1
        dept = ("ALL" if dept == "All Departments" else dept)
        search_content = request.GET["search_content"]
        course_result = CourseInfo.search_course_tool(search_content, dept, sort_option)
        context = {
            'search_results': course_result,
            'dept': dept,
            'search_content': search_content,
        }
    else:
        course_result = CourseInfo.objects.all()
        context = {
            'search_results': course_result,
            'dept': 'All Departments',
            'search_content': "",
        }
    paginator = Paginator(course_result, 10)
    page = request.GET.get('page', 1)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    except InvalidPage:
        return HttpResponse('Cannot find anything')
    context['search_results'] = courses
    print(course_result)

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
    if request.GET and 'search_content' in request.GET:
        print(request.GET)
        dept = request.GET["dept"].split(":")[1]
        dept = ("ALL" if dept == "All Departments" else dept)
        search_content = request.GET["search_content"]
        print(search_content)
        global prof_result
        if dept == "ALL":
            prof_result = ProfInfo.search_prof_tool(search_content)[:10]
        else:
            prof_result = ProfAndCourses.search_prof_by_dept(dept, search_content)[:10]
        for prof in prof_result: prof["dept"] = prof["dept"].replace('|', ' ')
        context = {
            'search_results': prof_result,
            'search_content': search_content,
        }
    else:
        prof_result = ProfInfo.objects.all()
        for prof in prof_result: prof.dept = prof.dept.replace('|', ' ')
        context = {
            'search_results': prof_result,
        }
    paginator = Paginator(prof_result, 10)
    if request.method == "GET":
        page = request.GET.get('page', 1)
        try:
            profs = paginator.page(page)
        except PageNotAnInteger:
            profs = paginator.page(1)
        except InvalidPage:
            return HttpResponse('Cannot find anything')
        except EmptyPage:
            profs = paginator.page(paginator.num_pages)
    context['search_results'] = profs
    return render(request, 'polls/search_faculty.html', context)


# Get professor home page
def prof_detail(request, name, db_id):
    result = ProfInfo.objects.filter(id=db_id)
    if len(result) == 1:
        prof = result[0]
    else:
        return Http404('Prof not found')
    courses = ProfAndCourses.search_course_by_prof(name)
    print(courses)
    context = {'prof_info': prof, 'prof_course': courses}
    return render(request, 'polls/faculty.html', context)

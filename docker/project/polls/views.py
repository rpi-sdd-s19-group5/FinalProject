from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

from info.models import CourseInfo, ProfAndCourses
from info.models import ProfInfo
from info.scripts.util_functions import search_related_links


# Rendering the main page
def index(request):
    return render(request, 'polls/main.html')


# Rendering the main faculty page
def index_prof(request):
    return render(request, 'polls/main_faculty.html')


# List the search results from required parameter
def search_course(request):
    # When the user writes something for searching
    if request.GET and "search_content" in request.GET:
        # print(request.GET)
        # get department
        dept = request.GET["dept"].split(":")[1]
        # 1 = alphabetical; 2 = course code; 3 = relevance
        # When user chooses to sort
        if "sort" in request.GET:
            sort_option = request.GET["sort"]
        else:
            sort_option = "1"
        # search all departments if no specific department
        dept = ("ALL" if dept == "All Departments" else dept)
        search_content = request.GET["search_content"]
        # use function to get the search result from CourseInfo
        course_result = CourseInfo.search_course_tool(search_content, dept, sort_option)
        dept = ("All Departments" if dept == "ALL" else dept)

        # Change to digit
        sort_option = (int(sort_option) if sort_option.isdigit() else 1)
        # context to send back
        context = {
            'search_results': course_result,
            'dept': dept,
            'search_content': search_content,
            'sort_option': sort_option - 1,
        }
    # When the user clicks searching without specifying the search content
    else:
        # get all info from CourseInfo
        course_result = CourseInfo.objects.all()
        context = {
            'search_results': course_result,
            'dept': 'All Departments',
            'sort_option': 0,
            'search_content': "",
        }
    # paging the result with 10 items in a page
    paginator = Paginator(course_result, 10)
    page = request.GET.get('page', 1)
    try:
        courses = paginator.page(page)
    # show the first page if not a well-formed page num
    except PageNotAnInteger:
        courses = paginator.page(1)
    # show the last page if no page exists
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    # show error info when no valid page exists
    except InvalidPage:
        return HttpResponse('Cannot find anything')
    context['search_results'] = courses
    # print(course_result)

    return render(request, 'polls/search_course.html', context)


# List the detail information of course
def course_detail(request, name_num):
    # filter out the course with specific course code
    course = CourseInfo.objects.filter(course_code=name_num)
    if len(course) == 1:
        # give related links to the user
        related_links = search_related_links(course[0])
        context = {'course_info': course[0],
                   'related_links': related_links}
        return render(request, 'polls/course.html', context)
    else:
        return Http404('Course not found')


# List all related professors
def search_prof(request):
    if request.GET and 'search_content' in request.GET:
        # print(request.GET)
        # get the department
        dept = request.GET["dept"].split(":")[1]
        # print(dept)
        # search all department if no specific one
        dept = ("ALL" if dept == "All Departments" else dept)
        search_content = request.GET["search_content"]
        # search for the result
        if dept == "ALL":
            prof_result = ProfInfo.search_prof_tool(search_content)
        else:
            prof_result = ProfAndCourses.search_prof_by_dept(dept, search_content)
        # formatting the faculty department
        for prof in prof_result:
            prof["dept"] = prof["dept"].replace('|', ' ')
        dept = ("All Departments" if dept == "ALL" else dept)
        context = {
            'search_results': prof_result,
            'search_content': search_content,
            'dept': dept,
        }
    # show all info in ProfInfo
    else:
        prof_result = ProfInfo.objects.all()

        for prof in prof_result:
            prof.dept = prof.dept.replace('|', ' ')
        context = {
            'search_results': prof_result,
            'dept': "All Departments",
        }
    # start paging the result with 10 items in a page
    paginator = Paginator(prof_result, 10)
    page = request.GET.get('page', 1)
    try:
        profs = paginator.page(page)
    # show the first page if not a valid page number
    except PageNotAnInteger:
        profs = paginator.page(1)
    # show the last page if no page exists
    except EmptyPage:
        profs = paginator.page(paginator.num_pages)
    # show the error info if no valid page
    except InvalidPage:
        return HttpResponse('Cannot find anything')
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
    # show the courses taught by faculty
    context = {'prof_info': prof, 'prof_course': courses}
    return render(request, 'polls/faculty.html', context)

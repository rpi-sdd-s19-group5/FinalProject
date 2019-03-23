from .models import CourseInfo
from .course_info import course_info_crawler

if __name__ == '__main__':
    course_info = course_info_crawler()
    for course in course_info:
        c = CourseInfo()
        c.title = course["title"]
        c.description = course["description"]
        c.prerequisites = course["prerequisites"]
        c.offered = course["offered"]
        c.cross_listed = course["cross_listed"]
        c.credit_hours = course["credit_hours"]
        c.save()

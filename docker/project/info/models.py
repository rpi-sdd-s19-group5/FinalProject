from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class CourseInfo(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20, default=None)
    dept = models.CharField(max_length=20, default=None)
    description = models.TextField(null=True, blank=True)
    prerequisites = models.TextField(null=True, blank=True)
    offered = models.CharField(max_length=100, null=True, blank=True)
    cross_listed = models.CharField(max_length=200, null=True, blank=True)
    credit_hours = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class ProfInfo(models.Model):
    url = models.URLField(blank=True, null=True, max_length=255)
    name = models.CharField(max_length=100)
    title = models.TextField(blank=True, null=True)
    dept = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    web_page = models.URLField(blank=True, null=True, max_length=255)
    focus = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True, max_length=255)

    # Update time
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class ProfAndCourses(models.Model):
    course_code = models.CharField(max_length=20, default="")
    dept = models.TextField()
    code_digit = models.TextField()
    prof = models.TextField()
    section = models.TextField()
    credit = models.TextField()
    days = models.TextField()
    time = models.TextField()
    date = models.TextField()
    location = models.TextField()

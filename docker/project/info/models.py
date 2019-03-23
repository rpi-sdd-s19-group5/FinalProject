from django.db import models


# Create your models here.
class CourseInfo(models.Model):
    title = models.CharField(max_length=200)
    dept = models.CharField(max_length=20, default="")
    course_code = models.CharField(max_length=20, default="")
    description = models.TextField()
    prerequisites = models.TextField()
    offered = models.TextField()
    cross_listed = models.TextField()
    credit_hours = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

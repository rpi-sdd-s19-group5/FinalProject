from django.db import models


# Create your models here.
class CourseInfo(models.Model):
    title = models.CharField(max_length=200)
    # dept = models.CharField(max_length=20)
    # course_id = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    prerequisites = models.TextField(null=True, blank=True)
    offered = models.CharField(max_length=100, null=True, blank=True)
    cross_listed = models.CharField(max_length=200, null=True, blank=True)
    credit_hours = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

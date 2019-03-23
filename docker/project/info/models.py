from django.db import models


# Create your models here.
class CourseInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    prerequisites = models.CharField(max_length=50)
    offered = models.CharField(max_length=20)
    cross_listed = models.CharField(max_length=50)
    credit_hours = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

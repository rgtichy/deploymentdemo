from __future__ import unicode_literals

from django.db import models
from ..userloginreg.models import User
# Create your models here.

#This is not working for me....
class CourseExtendedManager(models.Manager):
    def ECsave(ECobj):
        courseObject = Course.objects.get(id = ECobj.course_id)
        courseObject.title = ECobj.course.title

        courseExtendedObject = CourseExtended.objects.get(course_id = ECobj.course_id)
        courseExtendedObject.description = ECobj.description
        try:
            courseObject.save()
            courseExtendedObject.save()
            return True
        except:
            return False

class Course(models.Model):
    title = models.CharField(max_length = 70, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ManyToManyField(User)

class CourseExtended(models.Model):
    course = models.OneToOneField( Course, on_delete = models.CASCADE, primary_key = True )
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=CourseExtendedManager()

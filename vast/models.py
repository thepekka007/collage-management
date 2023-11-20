from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    fee = models.IntegerField()

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    jdate = models.DateField()
 
class teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    age = models.IntegerField()
    address = models.TextField(max_length=255)
    number = models.TextField(max_length=255)
    
    image = models.ImageField(upload_to="image/",null=True)
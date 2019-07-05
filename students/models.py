from django.db import models
from django.urls import reverse
class StudentProfile(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()

    def get_absolute_url(self):
        return  reverse('students:index')
    #photo= models.FileField()
    #def __str__(self):
       # return self.fname

class studentMarks(models.Model):
    sid = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    marks1 = models.IntegerField()
    marks2 = models.IntegerField()
    marks3 = models.IntegerField()



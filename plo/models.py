from django.db import models
from django.urls import reverse

# Create your models here.
class customer(models.Model):
    user_name=models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default="example@example.com")

    def get_absolute_url(self):
        return reverse('plo:index')
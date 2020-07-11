from django.db import models
from django.urls import reverse


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    #if we want to print School any moment the name will be printed out
    def __str__(self):
        return self.name

    #functtion related to createschoolview
    def get_absolute_url(self):
        return reverse("schoolapp:schooldetail", kwargs={"pk": self.pk})
    

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    #if we want to print School any moment the name will be printed out
    def __str__(self):
        return self.name
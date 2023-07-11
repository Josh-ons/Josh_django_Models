from __future__ import unicode_literals
from django.db import models


class Register(models.Model):
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O','Optimus Prime')
    )
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    Date = models.DateField(max_length=30)
    Age = models.IntegerField()
    upload = models.ImageField(max_length=30)

    class Meta:
        db_table = "student"

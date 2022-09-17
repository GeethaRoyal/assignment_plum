from statistics import mode
from django.db import models

# Create your models here.
class Organisation(models.Model):
    org_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)

class Members(models.Model):
    GENDER = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHERS', 'Others')
    ]
    org = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='members')
    employee_id = models.IntegerField(primary_key=True)
    email_id = models.EmailField(default=None)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default=None, blank=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)

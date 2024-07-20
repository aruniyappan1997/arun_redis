from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class EmployeesData(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    mobile = models.CharField(
        max_length=255)
    city = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

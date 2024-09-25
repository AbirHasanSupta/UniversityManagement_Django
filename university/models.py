from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

def age_validator(age):
    if not (18 <= age <= 100):
        raise ValidationError("Age must be between 18 and 100")


class Departments(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]


class Courses(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["department", "name"]

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
    code = models.CharField(max_length=5)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["department", "name"]

class Teachers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField(validators=[age_validator])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    course = models.ManyToManyField(Courses, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["department", "name"]


class Students(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    registration_id = models.IntegerField(unique=True, default=00000000)
    age = models.IntegerField(validators=[age_validator])
    date_of_birth = models.DateTimeField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    course = models.ManyToManyField(Courses, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["department", "registration_id"]
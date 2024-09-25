from django.db import models
from university.models import age_validator, Departments, Courses


class Teachers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=50, default="Lecturer")
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

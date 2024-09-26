from django.db import models
from university.models import age_validator, Departments, Courses
from .form_validation import registration_validator

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
    registration_id = models.CharField(max_length=8, unique=True, validators=[registration_validator])
    date_of_birth = models.DateTimeField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    course = models.ManyToManyField(Courses, blank=True)
    password = models.CharField(max_length=500, default="1234")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["department", "registration_id"]

    def save(self, *args, **kwargs):
        if self.pk:
            prev_student = Students.objects.get(pk=self.pk)
            if prev_student.department != self.department:
                self.course.clear()
        super(Students, self).save(*args, **kwargs)

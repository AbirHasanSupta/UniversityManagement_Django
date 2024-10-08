from django.db import models
from university.models import age_validator, Departments, Courses
from .form_validation import registration_validator

class Teachers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500, default="abcd")
    designation = models.CharField(max_length=50,choices=[
        ('teaching_assistant', 'Teaching Assistant'),
        ('lecturer', 'Lecturer'),
        ('assistant_professor', 'Assistant Professor'),
        ('associate_professor', 'Associate Professor'),
        ('professor', 'Professor'),
    ], default="lecturer")
    age = models.IntegerField(validators=[age_validator])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    course = models.ManyToManyField(Courses, blank=True, related_name="teachers")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["department", "designation", "name"]

    def save(self, *args, **kwargs):
        if self.pk:
            prev_teacher = Teachers.objects.get(pk=self.pk)
            if prev_teacher.department != self.department:
                self.course.clear()
        super(Teachers, self).save(*args, **kwargs)


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

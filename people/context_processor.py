from .models import Students, Teachers
import datetime

def people_processor(request):
    students = Students.objects.all()
    teachers = Teachers.objects.all()
    return {
        "students" : students,
        "teachers" : teachers,
        "current_year" : datetime.datetime.now().year
    }

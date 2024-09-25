from .models import Students, Teachers

def people_processor(request):
    students = Students.objects.all()
    teachers = Teachers.objects.all()
    return {
        "students" : students,
        "teachers" : teachers
    }

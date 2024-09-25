from university.models import Departments, Courses, Students, Teachers


def university_processor(request):
    departments = Departments.objects.all()
    courses = Courses.objects.all()
    students = Students.objects.all()
    teachers = Teachers.objects.all()
    return {
        "departments" : departments,
        "courses" : courses,
        "students" : students,
        "teachers" : teachers
    }

from university.models import Departments, Courses

def university_processor(request):
    departments = Departments.objects.all()
    courses = Courses.objects.all()

    return {
        "departments" : departments,
        "courses" : courses,
    }

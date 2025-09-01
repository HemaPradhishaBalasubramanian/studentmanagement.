from django.http import JsonResponse
from .models import Student

# Get all students
def student_list(request):
    students = Student.objects.all().values()  # values() → returns dict instead of model
    return JsonResponse(list(students), safe=False)

# Get one student by id
def student_detail(request, id):
    try:
        student = Student.objects.values().get(id=id)
        return JsonResponse(student, safe=False)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)

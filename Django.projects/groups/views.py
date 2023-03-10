from django.http import HttpResponse, Http404
from groups.models import Student
# Create your views here.

def first_view(request):
    # html = '<html><body><h1>John Snow</h1></body></html>'
    html = '<h1>John Snow</h1>'
    return HttpResponse(html)

def Students_view(request):
    info = Student.objects.all()
    html = ''
    for student in info:
        html += f'<h3>{student}</h3>'
    return HttpResponse(html)

def detail_student_view(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404("Student Not Found!")
    return HttpResponse(f'<h2>{student}</h2><p>{student.contacts} -- {student.passport}</p> ')

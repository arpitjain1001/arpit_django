from django.shortcuts import render,HttpResponse
from vege.models import Student,Subjectmarks
from django.db.models import Q

# Create your views here.


def hello(request):
    student_obj = Student.objects.all()
    # if request.GET.get('search'):
    #     search = request.GET.get('search')
    # student_obj = student_obj.filter(
    # Q(student_name__icontains = search) |
    # Q(department__department__icontains = search) |
    # Q(student_id__student_id__icontains = search) |
    # Q(student_age__icontains = search) |
    # Q(student_email__icontains = search)
    # )
    return render(request, "hello.html",{'queryset':student_obj})
 



def see_marks(request , student_id):
    student_obj=Subjectmarks.objects.all()
    student_obj=student_obj.filter(student__student_id__student_id = student_id)
    return render(request,"D:\\dj\\test\\foodie\\vege\\template\\see_marks.html" ,{'queryset':student_obj})




 
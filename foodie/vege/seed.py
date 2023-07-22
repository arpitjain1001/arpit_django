from faker import Faker 
fake = Faker()
import random
from .models import *
from django.db.models import Sum


# def create_subject_marks(n):
#     try:
#         student_objs = Student.objects.all()
#         for student in student_objs:
#             subjects = Subject.objects.all()
#             for subject in subjects:
#                 SubjectMarks.objects.create(
#                     subject = subject,
#                     student = student,
#                     marks = random.randint(0 , 100)
#         )
#     except Exception as e:
#         print(e)    


def seed_db(n=10) -> None:
    try:
        for i in range(0,n):
            departments_objs = Department.objects.all()
            random_index = random.randint(0,len(departments_objs)-1)
            student_id = f'STU-0{random.randint(100 , 999)}'
            department = departments_objs[random_index]
            student_name = fake.name()
            student_email =fake.email()
            student_age = random.randint(20 ,30)
            student_address = fake.address()


            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age =   student_age,
                student_address = student_address,
            
            )
    except Exception as e:
        print(e)




# def generate_report_card():
#      current_rank =-1
#      ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')
#      i = 1
#      for rank in ranks:
#         ReportCard.objects.create(
#         student = rank,
#         student_rank = i
#       )
#         i=i+1
 
# QUERIES 

# from vege.models import *
# queryset = Student.objects.filter(student_name_startswith ='a')
# queryset = Student.objects.filter(student_name_endswith ='a')
# queryset = Student.objects.filter(student_email ='org')
# queryset = Student.objects.filter(student_name_icontains ='An')
# queryset = Student.objects.filter(department__department__icontains ="Civ")
# d = ['Civil','Electrical']
# queryset = Student.objects.filter( department__in= d)
# queryset = Student.objects.exclude(department__department__icontains ="Civ") 

# from django.db.models import *
# from vege.models import *
# Students.objects.aggregate(Avg('student_age'))
# Students.objects.aggregate(Max('student_age'))
# Students.objects.aggregate(Min('student_age'))
# Students.objects.aggregate(Sum('student_age'))
# student = Student.objects.values('student_age').annotate(Count('student_age'))
# student = Student.objects.values('student_name').annotate(Count('student_age'))
# student = Student.objects.values('department',student_age).annotate(Count('department'),(Count('student_age')))

# python manage.py shell
# from vege.seed import *
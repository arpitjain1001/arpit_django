from django.db import models
from django.contrib.auth.models import User
from . models import *
# from . models import  Student
# from django.contrib.auth import get_user_model
# User = get_user_model()
# from .admin import total_marks

# Create your models here.
#MODELS:receipe,Department,StudentID,Subject, Student, SubjectMarks,ReportCard


# class receipe(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL ,null = True, blank=True)
#     receipe_name = models.CharField(max_length=100)
#     receipe_desc = models.TextField()
#     receipe_image = models.ImageField(upload_to = "receipe")
#     receipe_view_count =models.IntegerField(default=100)





class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
       return self.department

    class Meta:
        ordering = ['department']






class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
       return self.student_id
                                





class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
       return self.subject_name




class Student(models.Model):
     department = models.ForeignKey(Department , related_name="depart" ,on_delete=models.CASCADE)
     student_id = models.OneToOneField(StudentID , related_name="depart" ,on_delete=models.CASCADE)
     student_name = models.CharField(max_length=100)
     student_email = models.EmailField(unique=True)
     student_age = models.IntegerField(default=18)
     student_address= models.TextField()
     

     def __str__(self):
        return self.student_name 

     class Meta:
            ordering = ['student_name']
            verbose_name ='student' 





class Subjectmarks(models.Model):
     student= models.ForeignKey(Student , related_name="studentmarks" ,on_delete=models.CASCADE)
     subject_name = models.ForeignKey(Subject , related_name="studentmarks",on_delete=models.CASCADE)
     marks = models.IntegerField()
   
def __str__(self):
      return f'{self.student.student_name} {self.subject_name.subject_name}'

class Meta:
        unique_together = ['student','subject_name']






class Studentage(models.Model):
    student_age = models.IntegerField()

    def __str__(self):
       return self.student_age









# class ReportCard(models.Model):
#     student = models.ForeignKey(Student, related_name="studentreportcard",on_delete=models.CASCADE)
#     student_rank = models.IntegerField()
#     date_of_report_card_generation = models.DateField(auto_now_add=True)
#     total_marks=models.IntegerField()
    
#     class Meta:
#         unique_together = ['student_rank','date_of_report_card_generation']





    
    
from django.contrib import admin

# Register your models here.
from vege.models import StudentID,Student,Department,Subject,Studentage,Subjectmarks

# admin.site.register(receipe)

admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Studentage)
admin.site.register(Department)
# admin.site.register(ReportCard , ReportCardAdmin)
admin.site.register(Subject)
admin.site.register(Subjectmarks)
from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello),
    path('see_marks/<student_id>/',views.see_marks , name = 'see_marks')
]
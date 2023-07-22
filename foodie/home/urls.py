from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('home/',views.home),
    path('login/',views.login_page),
    path('register/',views.register),
    path('contact/',views.contact),
    path('logout/',views.logoutuser)
]

# https://qrcodebuilder.aseemgupta3.repl.co/
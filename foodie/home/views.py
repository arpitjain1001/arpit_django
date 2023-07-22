from django.shortcuts import render, HttpResponse, redirect
# from datetime import datetime
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "D:\\dj\\test\\foodie\\home\\template\\index.html")


def home(request):
    return render(request, "D:\\dj\\test\\foodie\\home\\template\\home.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        # mtlb isi username ka ek or insan(username) exists nhi krta hoga toh login page pae hi rhe vo  or agr kr jaega toh message sent username already taken
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect("/home/login/")

        # user = User.objects.create_user(username=username, password=password)

        # mtlb isi username ka yhi username h aur isi password ka yhi password h toh apnko vo authenticate krke de dega ki haa aap shi ho
        user = authenticate(username=username, password=password)

        if user is not None:  # mtlb yeh jo user h vo None nhi    vhi user h
            messages.success(request, "You are a user.")
            login(request, user=user)
            return redirect('/home/contact/')
        else:
            messages.error(request, "You are not a user.")
    return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(firstname)
        print(username)
        print(password)

        # ek hi naam ke 2 user nhi ho skte isley unique hona jaruri h
        if User.objects.filter(username=username).exists():
            # ab agr vo username exists krta h usi naam(username)ka toh message generate ho jaega ki yeh username alraedy hai toh vo register vaale page pae hi rhega

            messages.error(request, "Username alraedy taken")

            return redirect("/home/register/")

        user = User.objects.create(
            # firstname=firstname,
            username=username
        )
        user.set_password(password)  # password ko ase hi daalna h hmesha
        user.save()

        messages.success(request, "Account created successfully")

        return redirect('/home/login/')

    return render(request, 'D:\\dj\\test\\foodie\home\\template\\register.html')



# mtlb jb bhi apn contact page khole  toh sbse phele apn se vo login maange
@login_required(login_url="/home/login/")
def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        password = request.POST.get('password')
        print(name)
        print(email)
        # create
        contact = Contact(name=name, email=email, password=password, desc=desc)
        # mai isko ase bhi create kr skta hu

        contact.save()
        # Contact.object.create(name="arpit",email="arpit@gmail.com",password=1234,desc="you are a good boy")
        # contact.set_password(password)

        messages.success(request, "Your messages has been sent!.")
    return render(request, "contact.html")


# from django.contrib.auth.models import *
# User.objects.all()

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.conf import settings
from django.views.decorators.http import require_POST
from .models import User


# Create your views here.


def register_1(request):

    
    get_department_value=User.department_choices
    get_role_value=User.role_choices
    get_employee_value=User.employee_choices

    context={ 'get_department_value':get_department_value,
              'get_role_value':get_role_value, 
              'get_employee_value':get_employee_value,
            }


    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        image = request.FILES.get('profilepicture')
        birth_date=request.POST['birthdate']
        employee_joining_date=request.POST['employeejoiningdate']
        department=request.POST['department']
        role=request.POST['role']
        employee_type=request.POST['employeetype']

        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(
                    first_name=first_name, 
                    last_name=last_name, 
                    username=username, 
                    email=email,
                    password=password,
                    image=image,
                    birth_date=birth_date,
                    employee_joining_date=employee_joining_date,
                    department=department,
                    role=role,
                    employee_type=employee_type,

                    )
                user.save()
                return redirect('/')
        else:
            messages.error(request, 'password does not match')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html',context)


def login_1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('/dashboard')

            else:
                login(request, user)
                return redirect('/leaveform')

        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout_1(request):
    logout(request)
    return redirect('login')


def home_1(request):
    return render(request, 'logout.html')


def dashboard(request):

    return render(request, 'base.html')








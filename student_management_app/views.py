from curses.ascii import HT
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from student_management_app.EmailBackEnd import EmailBackEnd

def home(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method != 'POST':
        return HttpResponse('Methd Not Allowed')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type  == '1':
                return redirect('admin_home')

            elif user_type == '2':
                return redirect('staff_home')

            elif user_type == '3':
                return redirect('student_home')
            
            else:
                messages.error(request, 'Invalid login')
                
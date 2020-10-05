from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

def signupuser(request):
    if request.method == "GET" :
       return render(request,'todoapp/signupuser.html', {'form': UserCreationForm()})
    else :
        if request.POST['password1'] == request.POST['password2']:
            try:
               user= User.objects.create_user(request.POST['username'],request.POST['password1'])
               user.save()
               login(request, user)
               return redirect(currenttodos)
            except IntegrityError:
                return render(request, 'todoapp/signupuser.html', {'form': UserCreationForm(), 'error':'Username already exists Please give another name'})

        else:
           return render(request, 'todoapp/signupuser.html', {'form': UserCreationForm(), 'error':'Password didnot match'})

def currenttodos(request):
      return render(request, 'todoapp/currenttodos.html' )


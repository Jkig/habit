# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ToDoList, Item

'''
toDo = [
    {'id': 1, 'thing': "sqllite3"},
    {'id': 2, 'thing': "make this look decent enough"},
    {'id': 3, 'thing': "move this from a static object to a database"},
]
'''

def loginPage(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'username or password does not exist')

    context = {'page': page}
    return render(request, 'main/login_registration.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def registerNew(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit =False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Registration error')

    context = {'page': page, 'form': form}
    return render(request, 'main/login_registration.html', context)


def list1(request):
    toDo = Item.objects.all()  # TODO fix this, just display this user's stuff, also allow guests auto join..... 
    context = {'toDo': toDo}
    return render(request, "main/list.html", context)


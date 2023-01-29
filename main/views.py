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
    # TODO: fix this up, so eveyone can 
    # test for annother list by same user, and list from other user

    '''
    toDoList = ToDoList.objects.filter(user=request.user)
    all_Items = toDoList.item_set.all()
    '''



    # as_list = [i.item_set.all() for i in toDoList]
    # all_Items = []
    all_Items = toDoList[0].item_set.all()
    # for i in toDoList:
        # all_Items.append(i.item_set.all())


    # all_Items = toDoList.item_set.all() Works if i grabed toDoList from user, and user only has one, 
    # #     ex: toDoList = ToDoList.objects.get(user=request.user)# makes above line work
    # toDo = Item.objects.all() # every item in database lol
    context = {'toDo': all_Items}# , "full_list": full_list}
    return render(request, "main/list.html", context)


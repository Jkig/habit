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


def deleteItem(request, pk):
    item = Item.objects.filter(text=pk)[0]
    # messages.error(request, f'to-delete: {item.text}, {request.method}')
    item.delete()
    '''
    if request.method == "POST":
        item.delete()
        return redirect('/')
    '''
    return redirect('/')
    


def list1(request):
    # TODO: make it so that new users can interact...
    #   this is only able to add to the first todo list
    #   show all of a user's lists as seperate things, maybe push a list of lists of items: [[thing1, thing2, thing2], [thingA], [thingB]]

    # new items:

    # I think try everything below, and except send to a page where we can get it started


    toDoList = ToDoList.objects.filter(user=request.user)# gets queryset of all things

    if request.method == "POST":
        item = Item.objects.create(
            toDoList = toDoList[0],
            text = request.POST.get('new_item')
        )
        return redirect('/')
    
    all_Items = toDoList[0].item_set.all()
    for i in range(1,len(toDoList)):
        all_Items = all_Items.union(toDoList[i].item_set.all())

    context = {'toDo': all_Items}
    return render(request, "main/list.html", context)


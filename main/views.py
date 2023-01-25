from django.http import HttpResponse
from django.shortcuts import render

toDo = [
    {'id': 1, 'thing': "sqllite3"},
    {'id': 2, 'thing': "make this look decent enough"},
    {'id': 3, 'thing': "move this from a static object to a database"},
]


def list1(request):
    return render(request, "main/list.html", {'toDo': toDo})


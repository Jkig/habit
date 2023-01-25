from django.contrib import admin

# Register your models here.
from .models import ToDoList, Item  # , Room

admin.site.register(ToDoList)
admin.site.register(Item)

# DELETE THIS LATER< JUST TESTING SOME STUFF:
# admin.site.register(Room)

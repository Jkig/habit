from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    descripiton = models.CharField(max_length=300,null=True,blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
'''

class ToDoList(models.Model):
    # this is a list of Item objects, I need to figure out how to get this done in database, and get the admidmin fixed
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    numberOfItems = models.IntegerField(default=0)

class Item(models.Model):
    ToDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    #   not neccisary, as probs ppl won't be able to delete todo list, maybe they can, perhaps a main one they can't...

    # don't have this include a model, just have it include self,,, so its not a database shit, rather just an item....
    # todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    startTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)

    def __str__(self):
        return self.text

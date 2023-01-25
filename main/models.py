from django.db import models

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
    fullList = []

class Item(models.Model):
    # don't have this include a model, just have it include self,,, so its not a database shit, rather just an item....
    # todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    startTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)

    def __str__(self):
        return self.text

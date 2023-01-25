from django.db import models


# using his stuff for now... placeholder data stuff
'''
class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    descripiton = models.CharField(max_length=300)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_new_add=True)

    def __str__(self):
        return self.name
'''



'''
class ToDoList(models.Model):
    fullList = [] # this is a list of Item objects, I need to figure out how to get this done in database, and get the admidmin fixed


class Item(models.Model):
    # todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    startTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)

    def __str__(self):
        return self.text
'''
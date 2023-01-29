from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)



class Item(models.Model):
    toDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE, null=True)
    # todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300, null=True, blank=True)
    complete = models.BooleanField(default=False)
    startTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text

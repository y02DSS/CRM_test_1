from email.mime import image
from django.db import models
from django.contrib.auth.models import User
import json

class TypeRepair(models.Model):
    name = models.CharField(max_length=200) 

    def __str__(self):
        return self.name


class AllObjects(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Master(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)
    type_reair = models.OneToOneField(TypeRepair, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

 
class CompletedTask(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(AllObjects, on_delete=models.CASCADE)
    file = models.FileField(upload_to='static/uploads/files', blank=True, null=True)
    video = models.FileField(upload_to='static/uploads/video')
    comment = models.TextField()
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    home = models.ForeignKey(AllObjects, on_delete=models.CASCADE)
    problem = models.ForeignKey(TypeRepair, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
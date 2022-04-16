from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
    

class Room(models.Model): 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.body[0:50]
        

    
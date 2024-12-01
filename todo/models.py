from django.db import models
from django.contrib.auth.models import User 

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('INPR', 'In Progress'),
        ('DONE', 'Done'),
    ]

    gebruiker = models.ForeignKey(User, on_delete=models.CASCADE)  
    titel = models.CharField(max_length=200) 
    beschrijving = models.TextField(blank=True) 
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='TODO')
    aanmaakdatum = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.titel

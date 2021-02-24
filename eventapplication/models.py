from django.db import models
from django.contrib import admin

# Create your models here.
class Participant(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    instituition=models.CharField(max_length=50)

class ParticipantAdmin(admin.ModelAdmin):
    list_display=("username","email","phone")
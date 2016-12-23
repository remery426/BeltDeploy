from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User
from datetime import date
import datetime


class aptManager(models.Manager):
    def createapt(self,postData,user_id):
        response = {}
        errors = []
        if len(postData['task'])<1:
            errors.append("Please enter a task")
        if len(postData['aptdate'])<1:
            errors.append("Please enter a date")
        if postData['apttime']<1:
            error.append("Please Enter a time")
        try:
            datetime.datetime.strptime(postData['aptdate'], '%Y-%m-%d')
            print "Test try"
        except ValueError:
            errors.append("Please enter a valid date in the format YYYY-MM-DD")
        if errors:
            response['errors'] = errors
            response['check'] = False
            return response
        Appointment.objects.create(task = postData['task'], status = "Pending", date = postData['aptdate'], time = postData['apttime'], user = user_id)
        response['check']= True
        return response
    def editapt(self,postData,user_id):
        response = {}
        errors = []
        if len(postData['new_task'])<1:
            errors.append("Update failed not a task")
        if len(postData['new_date'])<1:
            errors.append("Update Failed not valid date")
        if postData['new_time']<1:
            errors.append("Update Failed not a valid time")
        try:
            datetime.datetime.strptime(postData['new_date'], '%Y-%m-%d')
            print "Test try"
        except ValueError:
            errors.append("Please enter a valid date in the format YYYY-MM-DD")
        if datetime.datetime.strptime(postData['new_date'], '%Y-%m-%d')<datetime.datetime.now():
            errors.append("Update failed. Not a valid date. Appointment cant be in past.")
        if errors:
            response['errors'] = errors
            response['check'] = False
            return response
        Appointment.objects.create(task = postData['new_task'], status = postData['new_status'], date = postData['new_date'], time = postData['new_time'], user = user_id)
        response['check']= True
        return response

class Appointment(models.Model):
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    user = models.ForeignKey('login_app.User')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = aptManager()
# Create your models here.

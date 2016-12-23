from __future__ import unicode_literals

from django.db import models
import re,  bcrypt
from datetime import date
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class userManager(models.Manager):
    def add_user(self, postData):
        errors = []
        if User.objects.filter(email=postData['email']):
            errors.append("Email is already registered")
        if len(postData['name'])<1 :
            errors.append("Name fields are mandatory!")
        if len(postData['email'])<1:
            errors.append("Email field is mandatory!")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Please enter a valid email!")
        if len(postData['password'])<8:
            errors.append("Password must contain at least 8 characters!")
        if(postData['password'] != postData['confirm_pass']):
            errors.append("Passwords must match!")
        if datetime.datetime.strptime(postData['date'], '%Y-%m-%d')>datetime.datetime.now():
            errors.append("Your birthday is not in the future")
        response = {}
        if errors:
            response['status'] = False
            response['error'] = errors
        else:
            response['status'] = True
            errors.append("You have registered successfully!")
            response['error']= errors
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            self.create(name=postData['name'], email=postData['email'], password=hashed,birthdate =postData['date'])
        return response
    def login_user(self, postData):
        errors_1 = []
        user = self.filter(email=postData['log_email'])
        if not user:
            errors_1.append("Email  is not registered")
        elif not bcrypt.checkpw(postData['log_pass'].encode(), user[0].password.encode()):
                errors_1.append("Invalid Email Password combination")
                print "Conditional Test"
        response_1 = {}
        if errors_1:
            response_1['status'] = False
            response_1['error']= errors_1
            print"Conditional 2"
        else:
            response_1['status']= True
            response_1['user']=user
        return response_1


class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length =100)
    birthdate  = models.DateField(null=True)
    updated_at = models.DateTimeField(auto_now_add =True)
    created_at = models.DateTimeField(auto_now = True)
    objects = userManager()

from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Appointment
from django.contrib import messages
import datetime
from datetime import date
# Create your views here.
def index(request):
    if request.session['thisuser']=='':
        return redirect('/')
    thisuser= User.objects.get(email=request.session['thisemail'])
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    todayapt =Appointment.objects.filter(user = thisuser, date__range=(today_min, today_max))
    myapt = Appointment.objects.filter(user = thisuser)
    context = {
        "apts" : myapt,
        "today" : todayapt,
        "Current_time" : datetime.datetime.now()
    }
    return render(request,"belt_app/index.html",context)
def logout(request):
    print"Test"
    request.session['thisuser']=''
    return redirect('/')
def createapt(request):
    print "Test"
    thisuser= User.objects.get(email=request.session['thisemail'])
    response = Appointment.objects.createapt(request.POST,thisuser)
    if not response['check']:
        for error in response['errors']:
            messages.error(request, error)
    return redirect('/belt_app/')

def delete(request,id):
    current_apt = Appointment.objects.get(id=id)
    current_apt= Appointment.objects.get(id=id).delete()
    return redirect('/belt_app/')
def editpage(request, id):
    request.session['edit_id'] = id
    editapt = Appointment.objects.get(id=id)
    context = {
        "apt" : editapt

    }
    return render(request,'belt_app/edit.html', context)
def edit(request,id):
    current_apt = Appointment.objects.get(id=id)
    thisuser= User.objects.get(email=request.session['thisemail'])
    response = Appointment.objects.editapt(request.POST,thisuser)
    if not response['check']:
        for error in response['errors']:
            messages.error(request, error)
            return redirect('/belt_app/')
    current_apt= Appointment.objects.get(id=id).delete()
    return redirect('/belt_app/')

from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User 

def index(request):

    records = User.objects.all()
    new_dict = {'user_records':records}
    return render(request,'help.html',context= new_dict)

def indexx(request):
    my_dict = {'user':'users'}
    return render(request,'home.html',context= my_dict)


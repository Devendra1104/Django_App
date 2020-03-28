from django.shortcuts import render
from django.http import HttpResponse
# from app_two.models import User 
from app_two.forms import NewUserForm

def indexx(request):
    my_dict = {'user':'users'}
    return render(request,'home.html',context= my_dict)



def index(request): #Users

    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return indexx(request)

        else:
            print("ERROR FORM INVALID")
    return render(request,'help.html',{'form':form})
    
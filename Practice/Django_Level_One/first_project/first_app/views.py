from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me':'Hello I am from first_app/index.html'}
    return render(request,'first_app/index.html',context=my_dict)

def help(request):
    my_dict2 = {'help_page':'Hello I am here to help'}
    return render(request,'first_app/help.html',context=my_dict2)

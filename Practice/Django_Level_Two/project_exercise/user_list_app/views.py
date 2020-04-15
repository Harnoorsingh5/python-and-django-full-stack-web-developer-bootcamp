from django.shortcuts import render
from django.http import HttpResponse
from user_list_app.models import Users

# Create your views here.

def index(request):
    # return HttpResponse("Hello")
    my_dict = {'insert_this': " Go to /users to see list of user information! "}
    return render(request,'user_list_app/index.html',context=my_dict)

def users(request):
    # return HttpResponse("Hello users")
    my_dict = {'user_list': Users.objects.all()}
    return render(request,'user_list_app/users.html',context=my_dict)
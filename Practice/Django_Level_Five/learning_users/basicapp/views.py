from django.shortcuts import render
from basicapp import forms

# 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse  
from django.contrib.auth.decorators import login_required
'''
    there are lot of decorators in DJnago to make life easier
    One of them is -> login_required
    If you ever wat the view that requires the user to be logged in you can decorate it with this 
'''
# Create your views here.
def index(request):
    my_dict = {"add_me":"Hello this is index.html"}
    return render(request, 'basicapp/index.html',context=my_dict)

def registration(request):

    registered = False

    # user_form = forms.UserForm()
    # profile_form = forms.UserProfileInfoForm()

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #Do something code
            
            user = user_form.save()
            user.set_password(user.password) #this function helps to save the password in hash format like SHA or bcrypt
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user # here we are setting the user mentioned in UserProfileInfo model (OneToOneField)
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True
        else:
             print(user_form.errors, profile_form.errors)

    else: #request is not an http req
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

             
    return render(request,'basicapp/registration.html',context={"user_form": user_form, "profile_form":profile_form, "registered":registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        '''Using Django inbuilt authenticate function login is easy'''
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not Active!")
        
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:        
        return render(request, 'basicapp/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required 
def special(request):
    return HttpResponse("You are logged in, Nice!")

'''
using this @login_required decorator Django makes sure that logout page or the particular 
page is only hit if the user is logged into the website
make the task easy for programmers.
'''
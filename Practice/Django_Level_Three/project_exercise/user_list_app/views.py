from django.shortcuts import render
from django.http import HttpResponse
from user_list_app.models import Users
from user_list_app import forms

# Create your views here.

def index(request):
    # return HttpResponse("Hello")
    my_dict = {'insert_this': " Go to /users to sign up! "}
    return render(request,'user_list_app/index.html',context=my_dict)

def users(request):
    # return HttpResponse("Hello users")
    form = forms.SignUpForm()

    # my_dict = {'user_list': Users.objects.all()}

    if request.method == 'POST':
         form = forms.SignUpForm(request.POST)
         
         if form.is_valid():
            #Do something code
            print("Validation success")
            print("FIRST NAME: " + form.cleaned_data['first_name'])
            print("LAST NAME: " + form.cleaned_data['last_name'])
            print("EMAIL: " + form.cleaned_data['email'])

            form.save(commit=True)
            return index(request)
         else:
             print("ERROR!")
             
    return render(request,'user_list_app/sign_up_form.html',context={"form": form})
# <-Django-> #
## Set up Django Project -> ##
while installing django -  it installs command line tool django-admin
to create Django project
django-admin startproject first_project
 
* __init__.py => blank python file that dues its special name let’s python know that dir can be treated as package
* settings.py => where we store all project settings
* urls.py => python script that will store all the URL patterns for your project. Basically different pages of your applications
* wigs.py =>  python script that acts as a web server gateway interface. It will later on help us deploy our web application to production. 

* manage.py => used a lot, helps associate with many commands as we build our web apps

## to run Django Server->##
python3 manage.py runserver

A Django project is a collection of applications and configurations that when combined together will make up full web applications (your complete website running under django).
A Django application is created to perform a particular functionality for your web application. For example, you may have a registration app, a polling app, comments app, etc.
These Django apps can be plugged into the Django projects, they can be reused.

## to  create Django app ->##
python manage.py startapp first_app
__init__.py => Blank python file that dues its special name let’s python know that dir can be treated as package
admin.py => You can register your model here which Django will then use them with Django’s admin interface.
apps.py => Here you can place any application specific configuration.
models.py => here you store application's data model.
tests.py => here you can store test functions to store your code
views.py => here you can store functions that handle request and return responses.
migration dir => this dir stores database specific info. as it relates to model.

To tell Django that we created the first app . We need to go to settings.py and add some  information about this app
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'first_app’,#like this
]

After all these steps->

##Step 1) Create a view ##
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")


		We can pass in some html inplace of Hello World

	#Step2) In order for us to see this view on Browser, we need to map this view in urls.py file
	
from django.contrib import admin
from django.urls import path
from first_app import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('first_app/', include('first_app.urls')),
]
	

Final url files are shown below (we need to create a unique url file for each application) (we need to map that url file in the projects urls.py file)

projects urls.py ->

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from first_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('first_app/', include('first_app.urls')),
]


applications urls.py ->

from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name="index"),
]



#Step3) Templates
are key parts of understanding how Django really works and interacts with your website
Contains static part of website that will always remain same
Template Tags - with special syntax - allows us to inject dynamic content that your Django Apps views will produce, effecting the final HTML
Firstly create a templates directory inside top level dir -> first_project/templates/first_app    - insert a file index.html in this
After this we have let Django know of templates by editing DIR key inside of TEMPLATES dictionary in the settings.py
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates') 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

index.html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>First App</title>
    </head>
    <body>
        <h1> Hello this is index.html </h1>
        {{ insert_me }}
    </body>
</html>

views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me':'Hello I am from first_app/index.html'}
    return render(request,'first_app/index.html',context=my_dict)



{{}} - text injection
{%%} - complex injection and logic

	#Step4) Adding static media files (photos) or css files
  

	create folder -> first_project/static/images


	add this path in settings.py file
STATIC_DIR = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]

	To load it in html file -> {% load static %}
	Then we insert he images using -> <img src = {% static “images/pic.jpg" %} />


<!DOCTYPE html>
{% load static %}
<html>
    <head>
        <meta charset="utf-8">
        <title>First App</title>
        <link rel="stylesheet" href="{% static "css/mystyle.css" %}"/>
    </head>
    <body>
        <h1> Hello this is index.html </h1>
        <h2> This is the picture of architecture of one of my project </h2>
        {{ insert_me }}
        <img src = "{% static "images/Architecture.png" %}" alt="not loading"/>
    </body>
</html>



#——————————————————————


#Models: 
We used models to incorporate a database into Django project.
Django comes equipped with SQLite. Django works with various other DBs.
Just need to change Engine parameter for DATABASES in settings.py file.
To create actual model, we use a class structure inside of relevant applications models.py file.
django.db.models.Model
Example of model class that will fo into models.py file of django app.


Each class acts as a table in the database.
inside each class we assign the column names of each table
After setting up models we can migrate databases, this basically let’s Django do heavy lifting of creating SQL databases that corresponds to models we created.
Django does all this with just one command ->  python manage.py migrate
Then register the changes to your app ->  python manage.py makemigrations app_name

in order to use more convenient admin interface with the models, we need to register them to our application’s admin.py file


Once the models and db are create we can use Django Admin interface to interact with db (which is one of key feature of Django)
In order to fully use db and admin, we need to create a super user using -> python manage.py createsuperuser

#Step1) edit models.py file to create table
from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)    
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

#Step2) To create tables we need to run few commands in sequence - 
Initiate:                           python3 manage.py migrate
register:                       

#Step3) Confirm whether it all works fine (using some shell commands)
open shell:                 python manage.py shell
                                      from first_app.models import Topic 
                                      print(Topic.objects.all())    ——> <QuerySet []>
                                     t = Topic(top_name="Social Network")  
                                     t.save() 
                                      print(Topic.objects.all())    ——> <QuerySet [<Topic: Social Network>]>

#Step4) Register models to admin.py file
from django.contrib import admin
from first_app.modelso import Topic,Webpage,AccessRecord
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)

In order to configure admin.py we need to create a super user for authorization and security purpose

python manage.py createsuperuser
				Username (leave blank to use 'harry'): harnoor
				Email address: harnoor.singh539@gmail.com
				Password: 
				Password (again): 
				This password is too short. It must contain at least 8 characters.
				This password is too common.
				This password is entirely numeric.
				Bypass password validation and cr

#Population Script:
We can add some dummy data in our tables using Faker library to create this script.
pip3 install Faker
https://faker.readthedocs.io/en/master/
create  file population_first_app.py
	Then configure settings for this project 
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

##FAKE PROP script
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker
import random

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    # retrieve the topic if it already exist or else it will create one
    # [0] bceacuse of the way it is formated - it returns a tuple that contains an object and we want reference to first model instance
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for entry
        top = add_topic()

        #create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create a Webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url =  fake_url)[0]

        # create a Access Record entry
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]


if __name__ == '__main__':
    print("Populating script")
    populate(20)


#Models - Templates - Views Paradigm
(MTV)
idea of how to connect everything
3 steps —>
In the views.py file import any models that we will need to use.
Use the view to query the model for data that we will need.
Pass results from model to template.
Edit the template so that it is ready to accept and display data from the model.
Map the url to the view

We can practice this methodology by changing what we display on front index page.
To begin our understanding of this process we will start by generating a table

—> starting

#Step1)
Opening views.py file to connect the db
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    # my_dict = {'insert_one': "Hello this is my view"}
    return render(request, 'first_app/index.html', context = date_dict)



go to index.html
<!DOCTYPE html>
{% load static %}
<html>
    <head>
    <meta charset="utf-8">
    <title> First App </title>
    <link rel="stylesheet" href="{% static "css/mystyle.css" %}"/>
    </head>
    <body>
     <h1> Hello this is index.html </h1>
     <h2> Here are your access records </h2>

     <div class = "recordtable">
     {% if access_records %}
        <table>
            <thead>
                <th>Site Name</th>
                <th>Date Accessed</th>
            </thead>
            {% for acc in access_records %}
            <tr>
                <td>{{acc.name}}</td>
                <td>{{acc.date}}</td>
            </tr>
            {% endfor %}
        </table>
     {% else %}
        <p>No access record found</p>
     {% endif %}
    </div>
    </body>
</html>


#Django Forms:

To create forms create a forms.py file in your application folder.
. After that call Django’s built in forms classes (very similar to creating models in Django)
. After cresting forms.py file we need to show it in our views.py class
		from . import forms
		from forms import formName
	(. indicates import from same dir)

—> Three type of requests when dealing with forms:
 HTTP: Hypertext transfer protocol and is designed to enable communication between client and server
	The client submits a request and server then responds to it
	Most commonly used methods for request/ response are GET and POST
GET - requests data from a resource
POST - submits data to be processed to a resource

we use CSRF - Cross Site Request Forgery token in our forms which secures the HTTP Post action that is initiated on the subsequent submission of a form.
{% csrf_token %}

#Step1) Create forms.py in app folder
from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)

#Step2) Modify views.py file
from django.shortcuts import render
from django.http import HttpResponse
from basicapp import forms

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    my_dict = {"add_me": "Go to /formpage to fill form"}
    return render(request, 'basicapp/index.html', context=my_dict)

def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something code
            print("Validation success")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])


    return render(request, 'basicapp/form_page.html', context={"form": form})
#Step3) form_page.html
<!DOCTYPE html>
<html>
    <head>
        <metad charset = "utf-8">
        <title>FORMS</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <div class="jumbotron">
                <h1 class="display-4"> This is a basic form app </h1>
                <hr class="my-4">
                <form class="form-group" method="post">
                    {{form.as_p}}
                    {% csrf_token %}
                     <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </body>
</html>
and adjust URLs accordingly


#Step4) Form validations:
We will learn three things here- Adding a check for empty fields	
Adding a check for a bot
Adding clean method for entire form
a) One way of doing validations -  by using clean method
from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT")
        return botcatcher



b) other way is by using Django’s in built methods:
from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])



c) you can also make your own custom validator:
from django import forms
from django.core import validators

# custom validator:
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("name need to start with z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT")
    #     return botcatcher


email check
from django.shortcuts import render
from django.http import HttpResponse
from basicapp import forms

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    my_dict = {"add_me": "Go to /formpage to fill form"}
    return render(request, 'basicapp/index.html', context=my_dict)

def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something code
            print("Validation success")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])


    return render(request, 'basicapp/form_page.html', context={"form": form})



#MODEL FORMS:
way to store the information into models/ DB

—> instead of using forms.Forms class —> use forms.ModelForm class in forms.py file
this helper class helps us to make forms out of existing  


forms.py // changes that need to be done
from django import forms
from user_list_app.models import Users

# custom validator:
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("name need to start with z")

class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 50) #(validators=[check_for_z]
    last_name = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 200)

    class Meta:
        model = Users
        fields = '__all__'



#Relative URLs with Templates:
So far we have used anchor tags with an href we’ve passed in a hardcoded path to the file.
This is a poor practice if we want our Django project to work on system

Usual :                                                                    <a href=“basic app/thankyou”> Thanks </a>
Can be changed to :                                            <a href=“{% url 'thanku'%}”> Thanks </a>  —> where name=’thanks’ is in urls.py
You could also just directly reference the view: <a href=“{% url ‘basic app.views.thankyou'%}”> Thanks </a> —> not used

relative_template_url.html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>HOME</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <div class="jumbotron">
                <h1 class="display-4"> Welcome! </h1>
                <hr class="my-4">
                <p class="lead">{{add_me}}</p>
                <a href="{% url 'basic_app:other' %}">The Other Page</a><br>
                <a href="{% url 'index' %}">Index Page</a><br>
                <a href="{% url 'admin:index' %}">Admin Page</a><br>
            </div>
        </div>
    <body>
</html>

index.html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>HOME</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <div class="jumbotron">
                <h1 class="display-4"> Welcome! </h1>
                <hr class="my-4">
                <p class="lead">{{add_me}}</p>
            </div>
        </div>
    <body>
</html>


other.html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>HOME</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <div class="jumbotron">
                <h1 class="display-4"> Welcome! </h1>
                <hr class="my-4">
                <p class="lead">{{add_me}}</p>
            </div>
        </div>
    <body>
</html>

views.py
from django.shortcuts import render

# Create your views here.
def index(request):
    mydict= {"add_me": "This is index.html"}
    return render(request,"basic_app/index.html", context=mydict)


def other(request):
    mydict= {"add_me": "This is other.html"}
    return render(request,"basic_app/other.html", context=mydict)

def relative(request):
    mydict= {"add_me": "This is relative_url_templates.html"}
    return render(request,"basic_app/relative_url_templates.html", context=mydict)

urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from basic_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('basic_app/', include('basic_app.urls')),
]

urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]




#URL Template Inheritance:
Main steps->
Find the repetitive part of your project
Create a base template for them
Set tags in base template
Extend and call the tags anywhere

—> base.html
	<link to JS, CSS, Bootstrap>
	<bunch of html like navbars>
		<body>
			{% block body_block %}
			{% endblock %}
		</body>
	</More footer html>

—> other.html
	<!DOCTYPE html>
	{% extends “basic_app/base.html” %}
	{% block body_block %}
		<HTML specific for other.html>
		<HTML specific for other.html>
	{% endblock %}
		


base.html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>HOME</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="{% url 'index' %}">BRAND</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">

            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="{% url 'admin:index' %}">Admin <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="{% url 'basic_app:other' %}">Other <span class="sr-only">(current)</span></a>
                </li>
            </ul>
        </nav>

        <div class="container">
            {% block body_block %}
            <!-- Anything outside of this will be inherited-->
            {% endblock %}
        </div>
    <body>
</html>

other.html

<!DOCTYPE html>
{% extends "basic_app/base.html" %}
{% block body_block %}
    <div class="jumbotron">
        <h1 class="display-4"> Welcome! </h1>
        <hr class="my-4">
        <p class="lead">{{add_me}}</p>
    </div>
{% endblock %}

index.html

<!DOCTYPE html>
{% extends 'basic_app/base.html' %}
{% block body_block %}
    <div class="jumbotron">
        <h1 class="display-4"> Welcome! </h1>
        <hr class="my-4">
        <p class="lead">{{add_me}}</p>
    </div>
{% endblock %}



#Template filters and custom filters:

inbuilt:
<p class="lead">{{number|add:"99"}}</p>

custom:
make a new directory named “templatetags” in application directory, create two files in that dir - > namely, __init__.py and my_extras.py

basic_app/templatetags/my_extras.py
from django import template

register = template.Library()

# one more way to register
@register.filter(name='cut')
def cut(value, arg):
    """
        This cuts out all values of arg from the String
    """
    return value.replace(arg, '')

# register.filter('cut',cut)


index.html
<!DOCTYPE html>
{% extends 'basic_app/base.html' %}
{% block body_block %}
{% load my_extras %}
    <div class="jumbotron">
        <h1 class="display-4"> Welcome! </h1>
        <hr class="my-4">
        <p class="lead">{{add_me}}</p>
        <p class="lead">{{text|cut:"World"}}</p>
        <p class="lead">{{number|add:"99"}}</p>
    </div>
{% endblock %}

view.py
from django.shortcuts import render

# Create your views here.
def index(request):
    mydict= {"add_me": "This is index.html", "text": "hello World!", "number": 10}
    return render(request,"basic_app/index.html", context=mydict)


def other(request):
    mydict= {"add_me": "This is other.html"}
    return render(request,"basic_app/other.html", context=mydict)

def relative(request):
    mydict= {"add_me": "This is relative_url_templates.html"}
    return render(request,"basic_app/relative_url_templates.html", context=mydict)


#Django Passwords: (Sign Up Page)

pip3 install crypt
python -m pip install argon2-cffi


settings.py
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length':9},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]

# MEDIA
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'




For images we use this fields type in our Model / DB ——>

“ImageField"
In order to work with images in Python, we need to install the python image library
pip3 install pillow
pip3 install pillow —global -option=“build_ext” —global -option=“—disable-jpeg”

Setup your model - in models.py
After setting model setup a user form - forms.py


#FIlES changes for Registration page:

models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE) # using the same fields from exiting user in django

    # add additional fields to User
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

    

forms.py
from django import forms
from django.contrib.auth.models import User
from basicapp import UserProfileInfo

class UserForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'passwords')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')



admin.py
from django.contrib import admin
from basicapp.models import UserProfileInfo
# Register your models here.

admin.site.register(UserProfileInfo)



views.py
from django.shortcuts import render
from basicapp import forms

# Create your views here.
def index(request):
    my_dict = {"add_me":"Hello this is index.html"}
    return render(request, 'basicapp/index.html',context=my_dict)

def login(request):
    my_dict = {"add_me":"Hello this is login.html"}
    return render(request, 'basicapp/login.html',context=my_dict)

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



registration.html

<!DOCTYPE html>
{% extends 'basicapp/base.html' %}
{% block body_block %}
    <div class="jumbotron">
        {% if registered %}
            <h1 class="display-4"> Thank you for registering! <h1>
        {% else %}
            <h1 class="display-4"> Register here! <h1>
            <h3 class="display-6"> Fill out form! </h3>
            <form class="form-group" method="post">
                {% csrf_token %}
                {{ user_form.as_p }}
                {{ profile_form.as_p }}
                <button type="submit" class="btn btn-primary">Register</button>
            </form>
        {% endif %}
    </div>
{% endblock %}


#FILES changed for login page

Process:
Setting up login views.
Using built in decorators for access.
Adding the LOGIN_URL in settings.
Creating the login.html
Editing urls.py


views.py —> add these eder files for setting up login functionality
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse  
from django.contrib.auth.decorators import login_required
'''
    there are lot of decorators in DJnago to make life easier
    One of them is -> login_required
    If you ever wat the view that requires the user to be logged in you can decorate it with this 
'''


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

settings.py —> string up login url
# LOGIN Settings
LOGIN_URL = '/basicapp/user_login’


login.html
<!DOCTYPE html>
{% extends 'basicapp/base.html' %}
{% load static %}
{% block body_block %}
    <div class="jumbotron">
        <h1 class="display-4"> Please Login </h1>
        <hr class="my-4">
        <form class="form-group" action="{% url 'basicapp:user_login' %}" method="post">
                {% csrf_token %}
                <label for="username">Username:</label>
                <input type="text" name="username" placeholder="Enter Username">
                <label for="password">Password:</label>
                <input type="password" name="password">
                <button type="submit" class="btn btn-primary">Sign In</button>
            </form>
    </div>
{% endblock %}


urls.py —>project’s url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from basicapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('basicapp/', include('basicapp.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
]


urls.py —> application’s url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('registration/', views.registration, name='registration'),
]


#DEPLOYING DJANGO WEBSITE:
simple hosting:
on —> pythonanywhere.com
(Digital ocean or Heroku)

Go to pythonanywhere.com -> go to console - bash
	run ->> mk virtualenv —python=python3.7 myproj      (where myproj is name of venv)
              ->> pip install -U django==‘your version number'
Get the link of git repository from GitHub.
	run  ->> git clone ’that link’

3.After cloning the repo you the server. Go to the project folder using cd commands
Then make migration
		->>  python manage.py migrate
		->> python manage.py makemigrations name_of_app
		->> run it one more time:  python3 manage.py migrate --run-syncdb
Then create SUPER user
		->> python manage.py createsuperuser

4.Go to your dash board -> then go to WEB tab -> click on ‘Add  new web app’ (follow some instruction (click on manual configurations))
Then do some manual config 
add virtual env (enter path to it) —> /home/whatever name is of project/.virtulenvs/whatever you have named your env
get ‘pwd’ of the project folder —> paste it in source code path 
setup wsgi config file —> setup path in this file
got to Django comment section
uncomment -> import os and import sys and path
path - ‘pwd’(replace it with pwd command result)
set settings.py path
then
import django
django.setup()

give static files path (admin and your own)
/static/admin and get it’s dir path
/static and add path to actual static folder

Go to settings.py and add ALLOWED_HOST=[ ’name of site or link of site’ ]
Set DEGUG=False



#CLASS BASED VIEWS: (CBV)
Previously we used function based views. However, Django provides a very powerful OOP concept of
class based views.


urls.py ——>
from django.contrib import admin
from django.urls import path,include
from cbv_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CBView.as_view()),
    path('cbv_app/', include('cbv_app.urls'))
]


views.py ——>

from django.views.generic import View # always import this 

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
# def index(request):
#     return render(request, 'cbv_app/index.html',context={"add_me":"Hello, this is index.html"})

class CBView(View):
    def get(self, request):
        return HttpResponse("Hello, this class based view")


#Template views with CBVs:

 difference between *args and **kwargs
    (kwargs - stand for keyword arguments)

    *args - gives all the function parameters as a tuple
          - just like varibale arguments
            def foo(*args):
                for a in args:
                    print(a)
            foo(1)     -> prints : 1
            foo(1,2,3) -> prints : 1 
				   2 
				   3
    
    **kwargs - gives keyword arguments,
             - gives you corresponding dictionaries, when you want to pass dictionaries as params
               def bar(**kwargs):
                   for a in kwargs:
                       print (a, kwargs[a])
                bar(name="one", age=27) -> prints: age 27
                                                   name one 


view.py ——>
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView

# Create your views here.
# def index(request):
#     return render(request, 'cbv_app/index.html',context={"add_me":"Hello, this is index.html"})

class CBView(View):
    def get(self, request):
        return HttpResponse("Hello, this class based view")

class IndexView(TemplateView):
    template_name = 'cbv_app/index.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_me"] = 'Hello, this is index.html' 
        return context
     



#Detail View and List View:
We have learned about Class Based Views to directly show a template.

Often when we have models, we want to either list the records from the model, or show details of a single record.

Previously, we did this with calls using Object Relation Mapper - 
MyModel.objects.all()

(one common practice - having template folder inside app’s folder)

1)

Create models first- 
models.py
from django.db import models

# Create your models here.
class School(models.Model):

    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


Register these models -
admin.py
from django.contrib import admin
from cbv_app.models import School,Student
# Register your models here.

admin.site.register(School)
admin.site.register(Student)



Run these commands-
->>  python3 manage.py migrate
->> python3 manage.py makemigrations name_of_app
->> run it one more time:  python3 manage.py migrate --run-syncdb

python3 manage.py createsuperuser

It is a common practice to make a template folder in each app (specific to each app)

(However, for common templates need to be placed in the templates folder outside of all other folders)

(app name)			(app name)
/cbv_app/template/cbv_app (make dir structure like this)

——> have created three .html files in this folder
cbv_app_base.html
school_detail.html
school_list.html

changes in views.py—>
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from cbv_app import models
# Create your views here.
# def index(request):
#     return render(request, 'cbv_app/index.html',context={"add_me":"Hello, this is index.html"})

class CBView(View):
    def get(self, request):
        return HttpResponse("Hello, this class based view")

class IndexView(TemplateView):
    template_name = 'index.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_me"] = 'Hello, this is index.html' 
        return context
        
'''
    ListView mentioned in views.py automatically creates and returns a variable which returns the list of all schools.
    Basically, it takes all the school from model School, and then store it in a list by following naming convention: 
    That is, it lower cases the name of the model and appends _list in the end.
   
    -> school_list  < nameofmodel_list  >

        class SchoolListView(ListView):
        model = models.School
        template_name = 'cbv_app/school_list.html' 

    -> or we can use the term --> object_list

'''
class SchoolListView(ListView):
    contect_object_name = 'schools'
    model = models.School
    # return a list named : school_list | after changing it returns a list named : schools

    # template_name = 'cbv_app/school_list.html' 

'''
    Details view returns the list as the lower case of model name
        i.e; school
   
    or we can use --> object
'''
class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'cbv_app/school_detail.html' 



changes in projects urls.py —>
from django.contrib import admin
from django.urls import path,include
from cbv_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view()),
    path('cbv_app/', include('cbv_app.urls'))
]


changes is app’s urls.py —>
from django.contrib import admin
from django.urls import path,include
from cbv_app import views

app_name = 'cbv_app'

urlpatterns = [
    # path('', views.IndexView.as_view()),
    path('',views.SchoolListView.as_view(), name='school_list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(), name='school_details'),
]
'''
    <int:pk>/ means that that it use the primary key of that model as the path to open the detail view of that particular item in list
'''

cbv_app_base.html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>HOME</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="{% url 'cbv_app:school_list' %}">Schools</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'admin:index' %}"> Admin <span class="sr-only">(current)</span></a>
                    </li>
                </ul>
            </div>
        </nav>

        <div class="container">
            {% block body_block %}

            {% endblock %}
        </div>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>

    <body>
</html>


school_list.html
<!DOCTYPE html>
{% extends 'cbv_app/cbv_app_base.html' %}
{% block body_block %}
    <div class="jumbotron">
        <h1 class="display-4"> This is list of all schools </h1>
        <hr class="my-4">
        <ol>
            {% for school in school_list %} 
                <h2 class="display-6"> <li> <a href="{{ school.id }}">{{ school.name }}</a></li> </h2>
            {% empty %}
                <h2 class="display-6"> <li>No Schools yet.</li> </h2>
            {% endfor %}
        </ol>
    </div>
{% endblock %}
<!--
    if you don't define a primary key
    Django give a default id as a primary key
    "school.id ""
-->
<!--
    Generally we would have used obhect.all to get the values from model
    However, list view does it automatically
    and makes it easy to access the records from model.
    Like this:

 -views.py
    from django.shortcuts import render
    from django.http import HttpResponse
    from first_app.models import Topic,Webpage,AccessRecord

    # Create your views here.

    def index(request):
        webpages_list = AccessRecord.objects.order_by('date')
        date_dict = {'access_records': webpages_list}

        # my_dict = {'insert_one': "Hello this is my view"}
        return render(request, 'first_app/index.html', context = date_dict)

- index.html
    <div class = "recordtable">
     {% if access_records %}
        <table>
            <thead>
                <th>Site Name</th>
                <th>Date Accessed</th>
            </thead>
            {% for acc in access_records %}
            <tr>
                <td>{{acc.name}}</td>
                <td>{{acc.date}}</td>
            </tr>
            {% endfor %}
        </table>
     {% else %}
        <p>No access record found</p>
     {% endif %}
    </div>
-->


school_detail.html
<!DOCTYPE html>
{% extends 'cbv_app/cbv_app_base.html' %}
{% block body_block %}
    <div class="jumbotron">
        <h1 class="display-4"> This is school details </h1>
        <hr class="my-4">
        <h2> School Details: </h2>
        <p> Name: {{ school.name }} </p>
        <p> Principal: {{ school.principal }} </p>
        <p> Location: {{ school.location }} </p>
        <h3 class="display-6"> Student: </h3>
            {% for student in school.students.all %}
                <p> {{student.name}}, who is {{ student.age }} years old. </p>
            {% empty %}
                <h2 class="display-6"> <li>No Students yet.</li> </h2>
            {% endfor %}
    </div>
{% endblock %}

<!-- 
    students.all is the related_name from Student Model defined in models.py class as shown below

    class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE) <<- over here

    def __str__(self):
        return self.name
-->


#CRUD views:

(Create Retrieve Update Delete)













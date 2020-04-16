"""cbv_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from cbv_app import views

app_name = 'cbv_app'

urlpatterns = [
    # path('', views.IndexView.as_view()),
    path('',views.SchoolListView.as_view(), name='school_list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(), name='school_details'),
    path('create/',views.SchoolCreateView.as_view(), name='school_create'),
    path('update/<int:pk>',views.SchoolUpdateView.as_view(), name='school_update'),
    path('delete/<int:pk>',views.SchoolDeleteView.as_view(), name='school_delete'),

]
'''
    <int:pk>/ means that that it use the primary key of that model as the path to open the detail view of that particular item in list
'''
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


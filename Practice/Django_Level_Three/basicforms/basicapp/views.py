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
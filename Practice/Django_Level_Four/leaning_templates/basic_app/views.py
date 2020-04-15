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
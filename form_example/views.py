from django.shortcuts import render
from .forms.exampleform import ExampleForm

# Create your views here.

def index(request):
    form = ExampleForm()
    return render(request, 'index.html', {"method": request.method, "form": form})

def form_example_get(request): 
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    
    return render(request, "form-example-get.html", {"method": request.method})

def form_example_post(request): 
    for name in request.GET:
        print("{}: {}".format(name, request.POST.getlist(name)))
    
    return render(request, "form-example-post.html", {"method": request.method})
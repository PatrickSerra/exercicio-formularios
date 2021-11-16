from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms.exampleform import ExampleForm
from .forms.exampleform2 import NameForm
from .forms.contactForm import ContactForm
from .forms.OrderForm import OrderForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    else:
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

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
        
    return render(request, 'name-form.html', {'form': form})

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():       
            print(form.cleaned_data)
            return HttpResponseRedirect('/contact-form')
    else:
        form = ContactForm()
        
    return render(request, 'contact-form.html', {'form': form})

def order_form(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        
        if form.is_valid():       
            print(form.cleaned_data)
            return HttpResponseRedirect('/order-form')
    else:
        form = OrderForm()
        
    return render(request, 'order-form.html', {'form': form})
    
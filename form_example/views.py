from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms.exampleform import ExampleForm
from .forms.RegisterForm import RegisterForm
from .forms.contactForm import ContactForm
from .forms.OrderForm import OrderForm
from .forms.RegisterModelForm import RegisterModelForm


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


def simple_form(request):
    print(request.POST)
    return render(request, 'simple-form.html')


def form_example_get(request): 
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    
    return render(request, "form-example-get.html", {"method": request.method})

def form_example_post(request): 
    for name in request.GET:
        print("{}: {}".format(name, request.POST.getlist(name)))
    
    return render(request, "form-example-post.html", {"method": request.method})

def register(request):
    if request.method == "POST":        
        registerForm = RegisterForm(request.POST)
        print(registerForm.is_bound)
        if registerForm.is_valid():
            print(registerForm.cleaned_data)
        
        else:
            print(registerForm.errors.as_data())
    
    else:
        registerForm = RegisterForm(initial={"nome_usuario": "Patrick", "sobrenome_usuario": "Serra"})    
        
    return render(request, 'register-form.html', {'form': registerForm})

def model_register(request):
    if request.method == "POST":
        registerForm = RegisterModelForm(request.POST)
        
        if registerForm.is_valid():
            print(registerForm.cleaned_data)
            registerForm.save()

        else:
            print(registerForm.errors.as_json())

    else:
        registerForm = RegisterModelForm()
    
    return render(request, 'register-model-form.html', {'form': registerForm})
    

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
    
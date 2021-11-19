from django import forms
from django.forms.widgets import Widget


class RegisterForm(forms.Form):
    nome_usuario = forms.CharField(
        label="Nome",
        error_messages={"required": "Por favor digite nome"}
        
    )
    nome_usuario.widget.attrs.update({'class': 'form-control'})
    
    sobrenome_usuario = forms.CharField(label="Sobrenome", label_suffix="?")
    
    
    sexo = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices= [("M", "Masculino"), ("F", "Feminino")],

    )
    
    data_de_nascimento = forms.DateField(
        #input_formats= ["DD/MM/YYYY"],
        error_messages= {
            "required":"Por favor, digite sua data de nascimento",
            "invalid": "Por favor, digite uma data válida" #mensagem que é mostrada caso a data seja inválida
        }
    )
    
    data_de_nascimento.widget.attrs.update({"type": "date"})
    
    email_usuario = forms.EmailField(initial="user@example.com", required=False)
    senha_usuario = forms.CharField(
        widget=forms.PasswordInput, 
        min_length=8, 
        error_messages={
            "min_length": "A senha deve conter no minimo oito caracteres",
            "required": "Por favor, digite uma senha"
        }
    )
    
    receber_newsletter = forms.BooleanField(required=False)
    
 
    
    
    
    #Ordem dos campos no formulário
    #field_order = ["nome_usuario","sobrenome_usuario", "senha_usuario", "email_usuario"]
    
    error_css_class = "error"
    required_css_class = "required"
    

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Field, Div, Submit, Button, Row, HTML
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator



class RegisterForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "formulario"
        self.helper.form_class = "classe-formulario"
        self.helper.form_action = ""
        self.helper.layout = Layout(
            Fieldset(
                "Informações Pessoais", #tag legend
                Field ("nome_usuario", id="nome-usuario", css_class="nome-usuario mb-2"),
                Field ("sobrenome_usuario", id="sobrenome-usuario", css_class="sobrenome-usuario mb-2"),
                Field ("sexo", id="sexo-usuario", css_class="sexo-usuario mb-3"),
                Field("data_de_nascimento", id="data-nascimento", type="date", css_class="data-nascimento  mb-2")
                
            ),
            
            Fieldset(
                "Informações de conta",
                Field("email_usuario", id="email-usuario", css_class="email-usuario mb-2"),
                Div(
                    Div(
                        Field("senha_usuario", id="senha-usuario", css_class="senha-usuario mb-2"), 
                        css_class = "col-sm-6"
                    ),
                    
                    Div(
                        Field("confirmar_senha", id="confirmar-senha", css_class="confirmar-senha mb-2"), 
                        css_class = "col-sm-6"
                    ),
                    css_class="row"
                ),
                Field("receber_newsletter", id="receber-newsletter", css_class="receber-newsletter mb-2"),
            ),
            
            Div(
                HTML(
                    """
                        <div> 
                            <input id="input-btn" type='submit' class='btn btn-outline-secondary'>
                            <input id="cancel-btn" type='submit' class='btn btn-outline-danger'>
                        </div>
                    """
                ),
                css_class="row mt-2"
            )
            
        )
    
    
    
    #valida se o campo não contém números ou carecteres especiais atráves de uma expressão regular
    NAME_VALIDATOR = RegexValidator(r'[^a-zA-Z]', message="esse campo não conter números e/ou caracteres especiais", inverse_match=True, code="entrada inválida")
    
    nome_usuario = forms.CharField(
        label="Nome",
        label_suffix= "",
        error_messages={"required": "Por favor digite seu nome"},
        validators=[NAME_VALIDATOR]
        
    )
 
    
    sobrenome_usuario = forms.CharField(
        label="Sobrenome", 
        label_suffix="",
        error_messages= {
            "required": "Por favor digite seu sobrenome nome"
        },
        validators=[NAME_VALIDATOR]
        
    )
    
    sexo = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices= [("M", "Masculino"), ("F", "Feminino")],
        required= False

    )
    
    data_de_nascimento = forms.DateField(
        #input_formats= ["DD/MM/YYYY"],
        error_messages= {
            "required":"Por favor, digite sua data de nascimento",
            "invalid": "Por favor, digite uma data válida" #mensagem que é mostrada caso a data seja inválida
        },
        required= False
    )
    
    
    email_usuario = forms.EmailField(
        initial="user@example.com", 
        required=False
    )
    
    senha_usuario = forms.CharField(
        label= "Senha",
        widget=forms.PasswordInput, 
        min_length=8, 
        error_messages={
            "min_length": "A senha deve conter no minimo oito caracteres",
            "required": "Por favor, digite uma senha"
        },
        required=False
    )
    
    confirmar_senha = forms.CharField(
        label= "Confirmar Senha",
        widget=forms.PasswordInput, 
        min_length=8, 
        error_messages={
            "min_length": "A senha deve conter no minimo oito caracteres",
            "required": "Por favor, digite uma senha"
        },
        required=False
    )
    
    receber_newsletter = forms.BooleanField(required=False)
    
    #Ordem dos campos no formulário
    #field_order = ["nome_usuario","sobrenome_usuario", "senha_usuario", "email_usuario"]
    
    def clean_nome_usuario(self):
        return self.cleaned_data['nome_usuario'].capitalize()
    
    def clean_sobrenome_usuario(self):
        return self.cleaned_data['sobrenome_usuario'].capitalize()
    
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha_usuario")
        confirmacao_senha = cleaned_data.get('confirmar_senha')
        
        print(senha)
        
        if senha != confirmacao_senha:
            raise ValidationError("As senhas não conferem")
            
        

from django.forms import forms, ModelForm, widgets
from django.forms.fields import CharField
from ..models import Usuario
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Field, Div, HTML


#Criar uma classe form
class RegisterModelForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "register-form"
        self.helper.form_class = "register-from"
        self.helper.form_action = ""
        self.helper.layout = Layout(
            Fieldset(
                "Informações Pessoais",  # tag legend
                Field("nome_usuario", id="nome-usuario",
                      css_class="nome-usuario mb-2"),
                Field("sobrenome_usuario", id="sobrenome-usuario",
                      css_class="sobrenome-usuario mb-2"),
                Field("sexo", id="sexo-usuario",
                      css_class="sexo-usuario mb-3"),
                Field("data_de_nascimento", id="data-nascimento",
                      type="date", css_class="data-nascimento  mb-2")

            ),

            Fieldset(
                "Informações de conta",
                Field("email_usuario", id="email-usuario",
                      css_class="email-usuario mb-2"),
                Div(
                    Div(
                        Field("senha_usuario", id="senha-usuario",
                              css_class="senha-usuario mb-2"),
                        css_class="col-sm-6"
                    ),

                    Div(
                        Field("confirmar_senha", id="confirmar-senha",
                              css_class="confirmar-senha mb-2"),
                        css_class="col-sm-6"
                    ),
                    css_class="row"
                ),
                
                Field("comentarios", id="comentarios-usuario",
                      css_class="email-usuario mb-2"),
                
                Field("receber_newsletter", id="receber-newsletter",
                      css_class="receber-newsletter mb-2"),
            ),

            Div(
                HTML(
                    """
                        <div>
                            <input id="input-btn" type='submit' class='btn btn-outline-secondary' value="enviar">
                            <input id="cancel-btn" type='button' class='btn btn-outline-danger' value="cancelar">
                        </div>
                    """
                ),
                css_class="row mt-2"
            )

        )

    
    NAME_VALIDATOR = RegexValidator(
        r'[^a-zA-Z]', message="esse campo não conter números e/ou caracteres especiais", inverse_match=True, code="nome inválido")
    
    nome_usuario = CharField(validators=[NAME_VALIDATOR])
    sobrenome_usuario = CharField(validators=[NAME_VALIDATOR])
    confirmar_senha = CharField(widget=widgets.PasswordInput)
   
    class Meta: 
        model = Usuario
        fields = '__all__'
        
        widgets = {
            "senha_usuario": widgets.PasswordInput(),
            "sexo": widgets.RadioSelect()
        }
        
        error_messages = {
            "email_usuario": {
                "unique": _("E-mail já cadastrado."),
                "required": _("Preencha este campo")
            }
        }
        
    def clean_nome_usuario(self):
        return self.cleaned_data['nome_usuario'].capitalize()
    
    def clean_sobrenome_usuario(self):
        return self.cleaned_data['sobrenome_usuario'].capitalize()
    
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha_usuario")
        confirmacao_senha = cleaned_data.get('confirmar_senha')
        
        if senha != confirmacao_senha:
            raise ValidationError("As senhas não conferem", code="senhas não conferem")
            
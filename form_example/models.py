from django.db import models
from django.forms import widgets
from django.utils import timezone

# Create your models here.


class Usuario(models.Model):

    SEX_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino")
    ]

    # USER_PREFERENCES = [
    #     ()
    # ]

    nome_usuario = models.CharField(max_length=30, help_text="Nome do Usuário", db_column="nome")
    sobrenome_usuario = models.CharField(max_length=30, help_text="Sobrenome do usuário", db_column="sobrenome")
    sexo = models.CharField(choices=SEX_CHOICES, default="Masculino", max_length=1, db_column="sexo")
    telefone_usuario = models.CharField(max_length=30, db_column="telefone")
    data_de_nascimento = models.DateField(db_column="dataNascimento")
    email_usuario = models.EmailField(help_text="Email do usuário", unique=True, db_column="email")
    senha_usuario = models.CharField(max_length=30, db_column="senha")
    receber_newsletter = models.BooleanField(db_column="newsletter")
    comentarios = models.TextField(blank=True)

    class Meta:
        db_table = "Usuario"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

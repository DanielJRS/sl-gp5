from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# cpf_validator = RegexValidator(r'^\d{11}$', _('CPF deve conter 11 dígitos numéricos.'))
# cep_validator = RegexValidator(r'^\d{8}$', _('CEP deve conter 8 dígitos numéricos.'))
# phone_validator = RegexValidator(r'^\d{8,9}$', _('Telefone deve ter 10 ou 11 dígitos (DDD + número).'))

class Login(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.email

class ClienteModel(models.Model):
    UF_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),  
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    nome = models.CharField(max_length=60)
    rg = models.CharField(max_length=14, blank=True, null=True)
    cpf = models.CharField(max_length=20,  unique=True)
    email = models.EmailField(max_length=60, blank=True, null=True)
    celular = models.CharField(max_length=20,  blank=True, null=True)
    telefone = models.CharField(max_length=20,  blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    uf = models.CharField(max_length=2, choices=UF_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"

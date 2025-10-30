from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ClienteModel

class CustomLoginForm(AuthenticationForm):
    pass

from django import forms
from .models import ClienteModel

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteModel
        fields = [
            'nome', 'rg', 'cpf', 'email', 'celular', 'telefone',
            'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo'
            }),
            'rg': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00.000.000-0'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00 (apenas números)'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 0000-0000'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000 (apenas números)'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rua, Avenida, etc.'
            }),
            'numero': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apto, Bloco, etc.'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade'
            }),
            'uf': forms.Select(attrs={ 
                'class': 'form-select',  
            }),
        }
        labels = {
            'nome': 'Nome Completo *',
            'rg': 'RG',
            'cpf': 'CPF *',
            'email': 'Email',
            'celular': 'Celular',
            'telefone': 'Telefone',
            'cep': 'CEP',
            'endereco': 'Endereço',
            'numero': 'Número',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'uf': 'UF',
        }

    def _only_digits(self, value):
        if value is None:
            return value
        return ''.join(ch for ch in str(value) if ch.isdigit())

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf:
            return cpf
        cpf_digits = self._only_digits(cpf)
        if len(cpf_digits) != 11:
            raise forms.ValidationError(f'CPF deve conter exatamente 11 dígitos numéricos. Encontrado: {len(cpf_digits)}')
        return cpf_digits

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if not cep:
            return cep
        cep_digits = self._only_digits(cep)
        if len(cep_digits) != 8:
            raise forms.ValidationError(f'CEP deve conter exatamente 8 dígitos numéricos. Encontrado: {len(cep_digits)}')
        return cep_digits

    def clean_celular(self):
        celular = self.cleaned_data.get('celular')
        if not celular:
            return celular
        celular_digits = self._only_digits(celular)
        if len(celular_digits) not in (10, 11):
            raise forms.ValidationError(f'Celular deve ter 10 ou 11 dígitos numéricos (DDD + número). Encontrado: {len(celular_digits)}')
        return celular_digits

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone:
            return telefone
        telefone_digits = self._only_digits(telefone)
        if len(telefone_digits) not in (10, 11):
            raise forms.ValidationError(f'Telefone deve ter 10 ou 11 dígitos numéricos (DDD + número). Encontrado: {len(telefone_digits)}')
        return telefone_digits

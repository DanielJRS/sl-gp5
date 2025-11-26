from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ClienteModel
from .models import funcionarioModel
from .models import FornecedorModel
from .models import VendaModel, ItemVendaModel
from django.forms import inlineformset_factory
from .models import VendaModel, ItemVendaModel


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
                'placeholder': '(apenas números)'
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
            'nome': 'Nome Completo',
            'rg': 'RG',
            'cpf': 'CPF ',
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
            raise forms.ValidationError(f'Encontrado: {len(cep_digits)}')
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


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = funcionarioModel
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
            'nome': 'Nome Completo',
            'rg': 'RG',
            'cpf': 'CPF',
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
    

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = FornecedorModel
        fields = '__all__'
        widgets = {
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
            'contato_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


from .models import ProdutoModel

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = ProdutoModel
        fields = '__all__'
        exclude = ['data_cadastro', 'data_atualizacao']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_barras': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'unidade_medida': forms.Select(attrs={'class': 'form-control'}),
            'estoque_atual': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estoque_minimo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estoque_maximo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'preco_custo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'preco_venda': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'margem_lucro': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'codigo': 'Código',
            'codigo_barras': 'Código de Barras',
            'nome': 'Nome do Produto',
            'descricao': 'Descrição',
            'categoria': 'Categoria',
            'unidade_medida': 'Unidade de Medida',
            'estoque_atual': 'Estoque Atual',
            'estoque_minimo': 'Estoque Mínimo',
            'estoque_maximo': 'Estoque Máximo',
            'preco_custo': 'Preço de Custo (R$)',
            'preco_venda': 'Preço de Venda (R$)',
            'margem_lucro': 'Margem de Lucro (%)',
            'fornecedor': 'Fornecedor',
            'ativo': 'Produto Ativo',
            'observacoes': 'Observações',
        }

class VendaForm(forms.ModelForm):
    class Meta:
        model = VendaModel
        fields = ['cliente', 'funcionario', 'forma_pagamento', 'desconto', 'status', 'observacoes']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'funcionario': forms.Select(attrs={'class': 'form-control'}),
            'forma_pagamento': forms.Select(attrs={'class': 'form-control'}),
            'desconto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'value': '0', 'min': '0', 'max': '100'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'cliente': 'Cliente',
            'funcionario': 'Vendedor',
            'forma_pagamento': 'Forma de Pagamento',
            'desconto': 'Desconto (%)',
            'status': 'Status da Venda',
            'observacoes': 'Observações',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = ClienteModel.objects.filter(ativo=True).order_by('nome')
        self.fields['funcionario'].queryset = funcionarioModel.objects.filter(ativo=True).order_by('nome')


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVendaModel
        fields = ['produto', 'quantidade', 'preco_unitario', 'desconto_item']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
            'preco_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'readonly': 'readonly'}),
            'desconto_item': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'value': '0', 'min': '0', 'max': '100'}),
        }
        labels = {
            'produto': 'Produto',
            'quantidade': 'Quantidade',
            'preco_unitario': 'Preço Unitário (R$)',
            'desconto_item': 'Desconto no Item (%)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = ProdutoModel.objects.filter(ativo=True).order_by('nome')
        
        if 'DELETE' in self.fields:
            self.fields['DELETE'].widget = forms.HiddenInput(attrs={'data-delete-input': 'true'})
            self.fields['DELETE'].initial = ''


ItemVendaFormSet = inlineformset_factory(
    VendaModel,
    ItemVendaModel,
    form=ItemVendaForm,
    fields=['produto', 'quantidade', 'preco_unitario', 'desconto_item'],
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
)

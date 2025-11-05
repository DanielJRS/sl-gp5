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
    


class funcionarioModel(models.Model):
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
        

class FornecedorModel(models.Model):
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
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    cnpj = models.CharField(max_length=20, unique=True)
    inscricao_estadual = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=60, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    uf = models.CharField(max_length=2, choices=UF_CHOICES, blank=True, null=True)
    contato_responsavel = models.CharField(max_length=60, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.razao_social} - {self.cnpj}"
    

class ProdutoModel(models.Model):
    UNIDADE_MEDIDA_CHOICES = [
        ('UN', 'Unidade'),
        ('CX', 'Caixa'),
        ('PC', 'Peça'),
        ('KG', 'Quilograma'),
        ('G', 'Grama'),
        ('L', 'Litro'),
        ('ML', 'Mililitro'),
        ('M', 'Metro'),
        ('CM', 'Centímetro'),
        ('M2', 'Metro Quadrado'),
        ('M3', 'Metro Cúbico'),
        ('DZ', 'Dúzia'),
        ('PCT', 'Pacote'),
        ('FD', 'Fardo'),
    ]
    
    CATEGORIA_CHOICES = [
        ('ALIMENTO', 'Alimentos'),
        ('BEBIDA', 'Bebidas'),
        ('HIGIENE', 'Higiene e Limpeza'),
        ('ELETRONICO', 'Eletrônicos'),
        ('VESTUARIO', 'Vestuário'),
        ('MOVEL', 'Móveis'),
        ('FERRAMENTA', 'Ferramentas'),
        ('MATERIAL', 'Material de Construção'),
        ('PAPELARIA', 'Papelaria'),
        ('OUTROS', 'Outros'),
    ]
    codigo = models.CharField(max_length=50, unique=True, help_text="Código interno do produto")
    codigo_barras = models.CharField(max_length=50, blank=True, null=True, help_text="Código de barras (EAN)")
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='OUTROS')
    unidade_medida = models.CharField(max_length=5, choices=UNIDADE_MEDIDA_CHOICES, default='UN')
    estoque_atual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estoque_minimo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estoque_maximo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    margem_lucro = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Margem de lucro em %")
    fornecedor = models.ForeignKey(
        'FornecedorModel', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        related_name='produtos'
    )
    ativo = models.BooleanField(default=True)
    observacoes = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
    
    def calcular_margem_lucro(self):
        """Calcula a margem de lucro percentual"""
        if self.preco_custo > 0:
            return ((self.preco_venda - self.preco_custo) / self.preco_custo) * 100
        return 0
    
    def estoque_baixo(self):
        """Verifica se o estoque está abaixo do mínimo"""
        return self.estoque_atual <= self.estoque_minimo


from django.utils import timezone

class VendaModel(models.Model):
    STATUS_CHOICES = [
        ('ORCAMENTO', 'Orçamento'),
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
        ('FINALIZADA', 'Finalizada'),
    ]
    
    FORMA_PAGAMENTO_CHOICES = [
        ('DINHEIRO', 'Dinheiro'),
        ('CARTAO_CREDITO', 'Cartão de Crédito'),
        ('CARTAO_DEBITO', 'Cartão de Débito'),
        ('PIX', 'PIX'),
        ('BOLETO', 'Boleto'),
        ('TRANSFERENCIA', 'Transferência Bancária'),
        ('CHEQUE', 'Cheque'),
        ('CREDIARIO', 'Crediário'),
    ]
    numero_venda = models.CharField(max_length=20, unique=True, editable=False)
    data_venda = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(
        'ClienteModel',
        on_delete=models.PROTECT,
        related_name='vendas'
    )
    funcionario = models.ForeignKey(
        'funcionarioModel',
        on_delete=models.PROTECT,
        related_name='vendas',
        verbose_name='Vendedor'
    )

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDENTE')
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO_CHOICES)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    observacoes = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Venda {self.numero_venda} - {self.cliente.nome}"
    
    def save(self, *args, **kwargs):
        if not self.numero_venda:
            ultimo = VendaModel.objects.order_by('-id').first()
            if ultimo:
                ultimo_numero = int(ultimo.numero_venda.split('-')[1])
                novo_numero = ultimo_numero + 1
            else:
                novo_numero = 1
            self.numero_venda = f"VND-{novo_numero:06d}"
        
        self.valor_total = self.subtotal - self.desconto
        
        super().save(*args, **kwargs)
    
    def calcular_totais(self):
        """Calcula o subtotal baseado nos itens da venda"""
        itens = self.itens.all()
        self.subtotal = sum(item.valor_total for item in itens)
        self.valor_total = self.subtotal - self.desconto
        self.save()
    
    def pode_cancelar(self):
        """Verifica se a venda pode ser cancelada"""
        return self.status in ['ORCAMENTO', 'PENDENTE']
    
    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ['-data_venda']


class ItemVendaModel(models.Model):
    venda = models.ForeignKey(
        'VendaModel',
        on_delete=models.CASCADE,
        related_name='itens'
    )
    produto = models.ForeignKey(
        'ProdutoModel',
        on_delete=models.PROTECT,
        related_name='itens_venda'
    )

    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    desconto_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    produto_nome = models.CharField(max_length=100)
    produto_codigo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.produto_nome} - Qtd: {self.quantidade}"
    
    def save(self, *args, **kwargs):
        if not self.produto_nome:
            self.produto_nome = self.produto.nome
            self.produto_codigo = self.produto.codigo
        
        if not self.preco_unitario:
            self.preco_unitario = self.produto.preco_venda
        
        self.valor_total = (self.quantidade * self.preco_unitario) - self.desconto_item
        
        super().save(*args, **kwargs)
        
        self.venda.calcular_totais()
    
    def delete(self, *args, **kwargs):
        venda = self.venda
        super().delete(*args, **kwargs)
        venda.calcular_totais()
    
    class Meta:
        verbose_name = "Item de Venda"
        verbose_name_plural = "Itens de Venda"
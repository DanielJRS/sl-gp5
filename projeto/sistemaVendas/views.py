import json
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import CustomLoginForm, ClienteForm, FuncionarioForm, FornecedorForm, ProdutoForm,  VendaForm, ItemVendaForm, ItemVendaFormSet
from django.http import HttpRequest
from django import forms
from .models import models,ClienteModel, funcionarioModel, FornecedorModel, ProdutoModel, VendaModel, ItemVendaModel
from django.db import models
from django.db import transaction
from django.contrib import messages
from django.db.models import Sum, Count, Q, F
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q

def loginForm(request):
    next_url = request.POST.get('next') or request.GET.get('next') or ''
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                    return redirect(next_url)
                return redirect('sistemaVendas:home')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form, 'next': next_url})

def _montar_contexto_dashboard():
    hoje = timezone.now()
    inicio_mes = hoje.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    mes_anterior = (inicio_mes - timedelta(days=1)).replace(day=1)

    total_clientes = ClienteModel.objects.count()

    total_produtos = ProdutoModel.objects.count()
    produtos_ativos = ProdutoModel.objects.filter(ativo=True).count()
    produtos_estoque_baixo = ProdutoModel.objects.filter(
        estoque_atual__lte=models.F('estoque_minimo')
    ).count()

    vendas_mes = VendaModel.objects.filter(
        data_venda__gte=inicio_mes,
        status__in=['CONFIRMADA']
    )
    total_vendas_mes = vendas_mes.aggregate(total=Sum('valor_total'))['total'] or 0
    qtd_vendas_mes = vendas_mes.count()

    vendas_mes_anterior = VendaModel.objects.filter(
        data_venda__gte=mes_anterior,
        data_venda__lt=inicio_mes,
        status__in=['CONFIRMADA']
    )
    total_vendas_mes_anterior = vendas_mes_anterior.aggregate(total=Sum('valor_total'))['total'] or 0

    if total_vendas_mes_anterior > 0:
        variacao_vendas = ((total_vendas_mes - total_vendas_mes_anterior) / total_vendas_mes_anterior) * 100
    else:
        variacao_vendas = 100 if total_vendas_mes > 0 else 0

    total_fornecedores = FornecedorModel.objects.count()
    fornecedores_com_produtos = FornecedorModel.objects.filter(
        produtos__isnull=False
    ).distinct().count()

    ultimas_vendas = VendaModel.objects.select_related(
        'cliente', 'funcionario'
    ).order_by('-data_venda')[:5]

    produtos_recentes = ProdutoModel.objects.select_related(
        'fornecedor'
    ).order_by('-data_cadastro')[:5]

    produtos_alerta = ProdutoModel.objects.filter(
        estoque_atual__lte=models.F('estoque_minimo'),
        ativo=True
    ).order_by('estoque_atual')[:5]

    return {
        'total_clientes': total_clientes,
        'total_produtos': total_produtos,
        'produtos_ativos': produtos_ativos,
        'produtos_estoque_baixo': produtos_estoque_baixo,
        'total_vendas_mes': total_vendas_mes,
        'qtd_vendas_mes': qtd_vendas_mes,
        'variacao_vendas': variacao_vendas,
        'total_fornecedores': total_fornecedores,
        'fornecedores_com_produtos': fornecedores_com_produtos,
        'ultimas_vendas': ultimas_vendas,
        'produtos_recentes': produtos_recentes,
        'produtos_alerta': produtos_alerta,
    }


@login_required
def home(request):
    contexto = _montar_contexto_dashboard()
    return render(request, 'home.html', contexto)


@login_required
def cliente_add(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sistemaVendas:cliente_home')
    else:
        formulario = ClienteForm()
    
    contexto = {'form': formulario}
    return render(request, 'templateCliente/Adicionarcliente.html', contexto)

@login_required
def cliente_home(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        clientes = ClienteModel.objects.filter(nome__icontains=query).order_by('nome')
    else:
        clientes = ClienteModel.objects.all().order_by('nome')
    
    contexto = {
        'clientes': clientes,
        'total_clientes': clientes.count(),
        'query': query
    }
    return render(request, 'templateCliente/homeCliente.html', contexto)

@login_required
def cliente_editar(request, cliente_id):
    cliente = get_object_or_404(ClienteModel, id=cliente_id)
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('sistemaVendas:cliente_home')
    else:
        formulario = ClienteForm(instance=cliente)
    
    contexto = {'form': formulario, 'cliente': cliente}
    return render(request, 'templateCliente/Adicionarcliente.html', contexto)

@login_required
def cliente_deletar(request, cliente_id):
    cliente = get_object_or_404(ClienteModel, id=cliente_id)
    cliente.delete()
    return redirect('sistemaVendas:cliente_home')


@login_required
def funcionario_home(request):
    query = request.GET.get('q', '').strip()
    if query:
        funcionarios = funcionarioModel.objects.filter(nome__icontains=query).order_by('nome')
    else:
        funcionarios = funcionarioModel.objects.all().order_by('nome')
    contexto = {
        'funcionarios': funcionarios,
        'total_funcionarios': funcionarios.count(),
        'query': query
    }
    return render(request, 'templatesFuncionario/homeFuncionario.html', contexto)


@login_required
def funcionario_add(request):
    if request.method == 'POST':
        formulario = FuncionarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sistemaVendas:funcionario_home')
    else:
        formulario = FuncionarioForm()
    
    contexto = {'form': formulario}
    return render(request, 'templatesFuncionario/adicionarFuncionario.html', contexto)


@login_required
def funcionario_editar(request, funcionario_id):
    funcionario = get_object_or_404(funcionarioModel, id=funcionario_id)
    if request.method == 'POST':
        formulario = FuncionarioForm(request.POST, instance=funcionario)
        if formulario.is_valid():
            formulario.save()
            return redirect('sistemaVendas:funcionario_home')
    else:
        formulario = FuncionarioForm(instance=funcionario)
    
    contexto = {'form': formulario, 'funcionario': funcionario}
    return render(request, 'templatesFuncionario/adicionarFuncionario.html', contexto)

@login_required
def funcionario_deletar(request, funcionario_id):
    funcionario = get_object_or_404(funcionarioModel, id=funcionario_id)
    funcionario.delete()
    return redirect('sistemaVendas:funcionario_home')


@login_required
def fornecedor_home(request):
    query = request.GET.get('q', '').strip()

    if query:
        fornecedores = FornecedorModel.objects.filter(
            Q(razao_social__icontains=query) | 
            Q(nome_fantasia__icontains=query)
        ).order_by('razao_social')
    else:
        fornecedores = FornecedorModel.objects.all().order_by('razao_social')
    
    contexto = {
        'fornecedores': fornecedores,
        'total_fornecedores': fornecedores.count(),
        'query': query
    }
    return render(request, 'templatesFornecedor/homeFornecedor.html', contexto)


@login_required
def fornecedor_add(request):
    if request.method == 'POST':
        formulario = FornecedorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sistemaVendas:fornecedor_home')
    else:
        formulario = FornecedorForm()
    
    contexto = {'form': formulario}
    return render(request, 'templatesFornecedor/adicionarFornecedor.html', contexto)


@login_required
def fornecedor_editar(request, fornecedor_id):
    fornecedor = get_object_or_404(FornecedorModel, id=fornecedor_id)
    if request.method == 'POST':
        formulario = FornecedorForm(request.POST, instance=fornecedor)
        if formulario.is_valid():
            formulario.save()
            return redirect('sistemaVendas:fornecedor_home')
    else:
        formulario = FornecedorForm(instance=fornecedor)
    
    contexto = {'form': formulario, 'fornecedor': fornecedor}
    return render(request, 'templatesFornecedor/adicionarFornecedor.html', contexto)


@login_required
def fornecedor_deletar(request, fornecedor_id):
    fornecedor = get_object_or_404(FornecedorModel, id=fornecedor_id)
    fornecedor.delete()
    return redirect('sistemaVendas:fornecedor_home')


@login_required
def produto_home(request):
    produtos = ProdutoModel.objects.all().order_by('nome')
    categoria = request.GET.get('categoria')
    estoque_baixo = request.GET.get('estoque_baixo')
    
    if categoria:
        produtos = produtos.filter(categoria=categoria)
    
    if estoque_baixo:
        produtos = produtos.filter(estoque_atual__lte=models.F('estoque_minimo'))
    
    contexto = {
        'produtos': produtos,
        'total_produtos': produtos.count(),
        'categorias': ProdutoModel.CATEGORIA_CHOICES,
        'categoria_selecionada': categoria,
        'estoque_baixo': estoque_baixo,
    }
    return render(request, 'templatesProduto/homeProduto.html', contexto)


@login_required
def produto_add(request):
    if request.method == 'POST':
        formulario = ProdutoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sistemaVendas:produto_home')
    else:
        formulario = ProdutoForm()
    
    contexto = {'form': formulario}
    return render(request, 'templatesProduto/adicionarProduto.html', contexto)


@login_required
def produto_editar(request, produto_id):
    produto = get_object_or_404(ProdutoModel, id=produto_id)
    if request.method == 'POST':
        formulario = ProdutoForm(request.POST, instance=produto)
        if formulario.is_valid():
            formulario.save()
            return redirect('sistemaVendas:produto_home')
    else:
        formulario = ProdutoForm(instance=produto)
    
    contexto = {'form': formulario, 'produto': produto}
    return render(request, 'templatesProduto/adicionarProduto.html', contexto)


@login_required
def produto_deletar(request, produto_id):
    produto = get_object_or_404(ProdutoModel, id=produto_id)
    produto.delete()
    return redirect('sistemaVendas:produto_home')


@login_required
def produto_detalhes(request, produto_id):
    produto = get_object_or_404(ProdutoModel, id=produto_id)
    contexto = {'produto': produto}
    return render(request, 'templatesProduto/detalhesProduto.html', contexto)

@login_required
@transaction.atomic
def venda_add(request):
    produtos_queryset = ProdutoModel.objects.filter(ativo=True).values(
        'id',
        'nome',
        'preco_venda',
        'estoque_atual',
        'unidade_medida'
    )
    produtos_json = json.dumps(list(produtos_queryset), cls=DjangoJSONEncoder)
    vendas = VendaModel.objects.select_related(
        'cliente',
        'funcionario'
    ).order_by('-data_venda')[:8]

    if request.method == 'POST':
        form = VendaForm(request.POST)
        formset = ItemVendaFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            venda = form.save()
            formset.instance = venda
            formset.save()
            
            for item in venda.itens.all():
                produto = item.produto
                produto.estoque_atual -= item.quantidade
                produto.save()
            
            messages.success(request, f'Venda {venda.numero_venda} criada com sucesso!')
            return redirect('sistemaVendas:venda_detalhes', venda_id=venda.id)
    else:
        form = VendaForm()
        formset = ItemVendaFormSet()
    
    contexto = {
        'form': form,
        'formset': formset,
        'produtos_json': produtos_json,
        'vendas': vendas,
    }
    return render(request, 'templateVenda/efetuarVenda.html', contexto)


@login_required
def venda_detalhes(request, venda_id):
    venda = get_object_or_404(VendaModel, id=venda_id)
    itens = venda.itens.all()
    desconto_percentual = Decimal(venda.desconto or 0)
    desconto_total_reais = (venda.subtotal or Decimal('0')) * (desconto_percentual / Decimal('100'))
    
    contexto = {
        'venda': venda,
        'itens': itens,
        'desconto_total_reais': desconto_total_reais,
    }
    return render(request, 'templateVenda/detalhesVenda.html', contexto)


@login_required
def venda_listar(request):
    status_filtro = request.GET.get('status', '').upper()
    vendas_queryset = VendaModel.objects.select_related('cliente', 'funcionario').order_by('-data_venda')

    if status_filtro:
        vendas_queryset = vendas_queryset.filter(status=status_filtro)

    total_valor = vendas_queryset.aggregate(total=Sum('valor_total'))['total'] or Decimal('0')

    contexto = {
        'vendas': vendas_queryset,
        'status_choices': VendaModel.STATUS_CHOICES,
        'status_filtro': status_filtro,
        'total_vendas': vendas_queryset.count(),
        'total_valor': total_valor,
    }
    return render(request, 'templateVenda/listarVendas.html', contexto)


@login_required
@transaction.atomic
def venda_editar(request, venda_id):
    venda = get_object_or_404(VendaModel, id=venda_id)
    produtos_queryset = ProdutoModel.objects.filter(ativo=True).values(
        'id',
        'nome',
        'preco_venda',
        'estoque_atual',
        'unidade_medida'
    )
    produtos_json = json.dumps(list(produtos_queryset), cls=DjangoJSONEncoder)
    vendas = VendaModel.objects.select_related(
        'cliente',
        'funcionario'
    ).order_by('-data_venda')[:8]
    
    if venda.status == 'CANCELADA':
        messages.error(request, 'Não é possível editar uma venda cancelada.')
        return redirect('sistemaVendas:venda_detalhes', venda_id=venda.id)
    
    for item in venda.itens.all():
        produto = item.produto
        produto.estoque_atual += item.quantidade
        produto.save()
    
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        formset = ItemVendaFormSet(request.POST, instance=venda)
        
        if form.is_valid() and formset.is_valid():
            venda = form.save()
            formset.save()
            
            for item in venda.itens.all():
                produto = item.produto
                produto.estoque_atual -= item.quantidade
                produto.save()
            
            messages.success(request, f'Venda {venda.numero_venda} atualizada com sucesso!')
            return redirect('sistemaVendas:venda_detalhes', venda_id=venda.id)
    else:
        form = VendaForm(instance=venda)
        formset = ItemVendaFormSet(instance=venda)
    
    contexto = {
        'form': form,
        'formset': formset,
        'venda': venda,
        'produtos_json': produtos_json,
        'vendas': vendas,
    }
    return render(request, 'templateVenda/efetuarVenda.html', contexto)


@login_required
@transaction.atomic
def venda_cancelar(request, venda_id):
    venda = get_object_or_404(VendaModel, id=venda_id)
    
    if not venda.pode_cancelar():
        messages.error(request, 'Esta venda não pode ser cancelada.')
        return redirect('sistemaVendas:venda_detalhes', venda_id=venda.id)
    
    if request.method == 'POST':
        for item in venda.itens.all():
            produto = item.produto
            produto.estoque_atual += item.quantidade
            produto.save()
        
        venda.status = 'CANCELADA'
        venda.save()
        
        messages.success(request, f'Venda {venda.numero_venda} cancelada com sucesso!')
        return redirect('sistemaVendas:venda_home')
    
    contexto = {'venda': venda}
    return render(request, 'templateVenda/cancelarVenda.html', contexto)


@login_required
def venda_deletar(request, venda_id):
    venda = get_object_or_404(VendaModel, id=venda_id)
    
    if venda.status != 'PENDENTE':
        messages.error(request, 'Apenas vendas pendentes podem ser deletadas. Use o cancelamento para outras situações.')
        return redirect('sistemaVendas:venda_detalhes', venda_id=venda.id)
    
    venda.delete()
    messages.success(request, 'Registro excluído com sucesso!')
    return redirect('sistemaVendas:venda_home')


def logout_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            auth_logout(request)
            messages.success(request, 'Você saiu do sistema com sucesso!')
        return redirect('sistemaVendas:login')
    return render(request, 'login.html')


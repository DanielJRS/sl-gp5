from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import CustomLoginForm, ClienteForm, FuncionarioForm
from django.http import HttpRequest
from django import forms
from .models import models,ClienteModel, funcionarioModel

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

@login_required
def home(request):
    return render(request, 'home.html')


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
    clientes = ClienteModel.objects.all().order_by('nome')
    contexto = {
        'clientes': clientes,
        'total_clientes': clientes.count()
    }
    return render(request, 'templateCliente/homeCliente.html', contexto)

@login_required
def cliente_editar(request, cliente_id):
    """Página para editar um cliente existente"""
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
    funcionarios = funcionarioModel.objects.all().order_by('nome')
    contexto = {
        'funcionarios': funcionarios,  
        'total_funcionarios': funcionarios.count()
    }
    return render(request, 'templatefuncionario/homefuncionario.html', contexto)


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
    return render(request, 'templatefuncionario/Adicionarfuncionario.html', contexto)


@login_required
def funcionario_editar(request, funcionario_id):
    """Página para editar um funcionário existente"""
    funcionario = get_object_or_404(funcionarioModel, id=funcionario_id)
    if request.method == 'POST':
        formulario = FuncionarioForm(request.POST, instance=funcionario)
        if formulario.is_valid():
            formulario.save()
            return redirect('sistemaVendas:funcionario_home')
    else:
        formulario = FuncionarioForm(instance=funcionario)
    
    contexto = {'form': formulario, 'funcionario': funcionario}
    return render(request, 'templatefuncionario/Adicionarfuncionario.html', contexto)

@login_required
def funcionario_deletar(request, funcionario_id):
    funcionario = get_object_or_404(funcionarioModel, id=funcionario_id)
    funcionario.delete()
    return redirect('sistemaVendas:funcionario_home')

# def cliente_add(request):
#     if request.method == 'POST':
#         formulario = ClienteForm(request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('sistemaVendas:cliente_home')
#     else:
#         formulario = ClienteForm()
    
#     contexto = {'form': formulario}
#     return render(request, 'templateCliente/Adicionarcliente.html', contexto)


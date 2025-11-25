from django.urls import path
from . import views

app_name = 'sistemaVendas'

urlpatterns = [
    path('', views.loginForm, name='login'),
	path('login/', views.loginForm, name='login'),
	path('home/', views.home, name='home'),

	# URL para cliente
	path('clientes/', views.cliente_home, name='cliente_home'),
	path('clientes/adicionar/', views.cliente_add, name='cliente_adicionar'),
    path('clientes/editar <int:cliente_id>/', views.cliente_editar, name='cliente_editar'),
    path('clientes/deletar/<int:cliente_id>/', views.cliente_deletar, name='cliente_deletar'),
    

	#URL para funcionário
    path('funcionario/', views.funcionario_home, name='funcionario_home'),
    path('funcionario/adicionar/', views.funcionario_add, name='funcionario_adicionar'),
    path('funcionario/editar/<int:funcionario_id>/', views.funcionario_editar, name='funcionario_editar'),
    path('funcionario/deletar/<int:funcionario_id>/', views.funcionario_deletar, name='funcionario_deletar'),

    #URL para fornecedor
    path('fornecedor/', views.fornecedor_home, name='fornecedor_home'),
    path('fornecedor/adicionar/', views.fornecedor_add, name='fornecedor_add'),
    path('fornecedor/editar/<int:fornecedor_id>/', views.fornecedor_editar, name='fornecedor_editar'),
    path('fornecedor/deletar/<int:fornecedor_id>/', views.fornecedor_deletar, name='fornecedor_deletar'),

    #URL para produto
    path('produto/', views.produto_home, name='produto_home'),
    path('produto/adicionar/', views.produto_add, name='produto_add'),
    path('produto/editar/<int:produto_id>/', views.produto_editar, name='produto_editar'),
    path('produto/deletar/<int:produto_id>/', views.produto_deletar, name='produto_deletar'),
    path('produto/detalhes/<int:produto_id>/', views.produto_detalhes, name='produto_detalhes'),

    #URL para venda
    path('venda/', views.venda_add, name='venda_home'),
    path('venda/adicionar/', views.venda_add, name='venda_add'),
    path('venda/listar/', views.venda_listar, name='venda_listar'),
    path('venda/detalhes/<int:venda_id>/', views.venda_detalhes, name='venda_detalhes'),
    path('venda/editar/<int:venda_id>/', views.venda_editar, name='venda_editar'),
    path('venda/cancelar/<int:venda_id>/', views.venda_cancelar, name='venda_cancelar'),
    path('venda/deletar/<int:venda_id>/', views.venda_deletar, name='venda_deletar'),

    #URL para configurações
    path('configuracoes/', views.configuracoes_view, name='configuracoes'),

    #URL para logout
    path('logout/', views.logout_view, name='logout'),

    #URL para relatorio 
    path('relatorios/', views.relatorio_home, name='relatorio_home'),

]

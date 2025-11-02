from django.urls import path
from . import views

app_name = 'sistemaVendas'

urlpatterns = [
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
]
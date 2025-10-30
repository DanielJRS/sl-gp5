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
]
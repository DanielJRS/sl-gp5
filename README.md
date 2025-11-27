# Sistema de vendas - SL-GPS

Sistema de gerenciamento de vendas desenvolvido com Django, permitindo o controle completo de clientes, fornecedores, produtos, funcionários e transações comerciais.

## Descrição

Aplicação web para gestão empresarial focada em operações de vendas, desenvolvida com Django framework seguindo arquitetura MVT (Model-View-Template). O sistema oferece funcionalidades completas para administração de vendas, controle de estoque e geração de relatórios gerenciais.

## Tecnologias utilizadas

- Python 3
- Django Framework
- PostgreSQL
- pgAdmin4
- HTML5
- CSS3
- JavaScript

## Estrutura do projeto

```
sl-gps/
├── projeto/                      # Configurações principais do Django
├── sistemavendas/                # Aplicação principal do sistema
│   ├── __pycache__/             # Cache compilado do Python
│   ├── migrations/              # Migrações do banco de dados
│   ├── templates/               # Templates HTML organizados por módulo
│   │   ├── templatecliente/    # Interface de gestão de clientes
│   │   │   ├── adicionarcliente.html
│   │   │   └── homecliente.html
│   │   ├── templaterelatorio/  # Interface de relatórios
│   │   │   └── homeRelatorio.html
│   │   ├── templatefornecedor/ # Interface de gestão de fornecedores
│   │   │   ├── adicionarfornecedor.html
│   │   │   └── homefornecedor.html
│   │   ├── templatefuncionario/# Interface de gestão de funcionários
│   │   │   ├── adicionarfuncionario.html
│   │   │   └── homeFuncionario.html
│   │   ├── templateproduto/    # Interface de gestão de produtos
│   │   │   ├── adicionarproduto.html
│   │   │   ├── detalhesProduto.html
│   │   │   └── homeProduto.html
│   │   ├── templatevenda/      # Interface de gestão de vendas
│   │   │   ├── detalhesVenda.html
│   │   │   ├── efetuarvenda.html
│   │   │   └── listarvendas.html
│   │   ├── home.html           # Dashboard principal
│   │   └── login.html          # Autenticação de usuários
│   ├── views/                   # Views organizadas por módulo
│   ├── __init__.py
│   ├── admin.py                 # Configuração do painel administrativo
│   ├── apps.py                  # Configuração da aplicação Django
│   ├── forms.py                 # Definição de formulários
│   ├── models.py                # Modelos de dados (ORM)
│   ├── tests.py                 # Suite de testes
│   ├── urls.py                  # Roteamento de URLs da aplicação
│   └── views.py                 # Views principais
├── .gitignore                   # Arquivos e diretórios ignorados pelo Git
├── db.sqlite3                   # Banco de dados de desenvolvimento
└── manage.py                    # Interface de linha de comando do Django
```

## Funcionalidades

### Módulo de clientes
- Cadastro de novos clientes
- Listagem e busca de clientes
- Edição de informações cadastrais
- Visualização de histórico de compras

### Módulo de fornecedores
- Registro de fornecedores
- Gerenciamento de contatos e informações comerciais
- Histórico de transações
- Busca e filtros avançados

### Módulo de produtos
- Cadastro de produtos com informações detalhadas
- Controle de estoque em tempo real
- Visualização de detalhes e especificações
- Gerenciamento de preços e categorias

### Módulo de funcionários
- Cadastro de funcionários
- Gerenciamento de perfis e permissões
- Controle de acesso ao sistema
- Histórico de atividades

### Módulo de vendas
- Processamento de transações de venda
- Emissão de comprovantes
- Histórico completo de vendas
- Controle de pagamentos

### Módulo de relatórios
- Relatórios de vendas por período
- Análise de desempenho
- Relatórios financeiros
- Exportação de dados

## Requisitos do sistema

### Pré-requisitos
- Python 3.8 ou superior
- PostgreSQL 12 ou superior
- pgAdmin4
- pip (gerenciador de pacotes Python)
- virtualenv ou venv

## Instalação

### 1. Clonar o repositório
```bash
git clone <url-do-repositorio>
cd sl-gps
```

### 2. Configurar ambiente virtual
```bash
python -m venv venv
```

Ativar ambiente virtual:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install django
pip install psycopg2-binary
pip install -r requirements.txt
```

### 4. Configurar banco de dados

Criar banco de dados PostgreSQL via pgAdmin4 ou terminal:

```sql
CREATE DATABASE sl_gps_db;
CREATE USER sl_gps_user WITH PASSWORD 'sua_senha';
ALTER ROLE sl_gps_user SET client_encoding TO 'utf8';
ALTER ROLE sl_gps_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE sl_gps_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE sl_gps_db TO sl_gps_user;
```

Configurar `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sl_gps_db',
        'USER': 'sl_gps_user',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Executar Migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Criar Superusuário
```bash
python manage.py createsuperuser
```

### 7. Coletar Arquivos Estáticos
```bash
python manage.py collectstatic
```

### 8. Iniciar Servidor de Desenvolvimento
```bash
python manage.py runserver
```

O sistema estará disponível em `http://127.0.0.1:8000/`

## Acesso ao Sistema

### Interface Principal
```
http://127.0.0.1:8000/
```

### Painel Administrativo
```
http://127.0.0.1:8000/admin/
```

Utilize as credenciais do superusuário criado na etapa de instalação.

## Modelos de Dados

### Cliente
Armazena informações cadastrais de clientes, incluindo dados pessoais, contatos e endereço.

### Fornecedor
Registra dados de fornecedores, informações comerciais e histórico de transações.

### Produto
Mantém catálogo de produtos com preços, estoque, descrições e categorias.

### Funcionário
Gerencia informações de funcionários e suas permissões de acesso ao sistema.

### Venda
Registra transações de venda, itens vendidos, valores e métodos de pagamento.

## Testes

Executar suite de testes:

```bash
python manage.py test
```

Executar testes com cobertura:

```bash
coverage run --source='.' manage.py test
coverage report
```

## Segurança

- Autenticação baseada em sessões Django
- Proteção CSRF habilitada
- Sanitização de inputs de usuário
- Controle de permissões por módulo
- Hash seguro de senhas com PBKDF2
- Proteção contra SQL Injection via ORM

## Deploy em Produção

### Configurações Recomendadas

1. Definir `DEBUG = False` em `settings.py`
2. Configurar `ALLOWED_HOSTS` adequadamente
3. Utilizar variáveis de ambiente para credenciais
4. Configurar servidor web (Nginx/Apache)
5. Utilizar WSGI server (Gunicorn/uWSGI)
6. Configurar SSL/TLS
7. Implementar backup regular do banco de dados

### Exemplo com Gunicorn

```bash
pip install gunicorn
gunicorn projeto.wsgi:application --bind 0.0.0.0:8000
```

## Contribuindo

### Fluxo de Contribuição

1. Fork o projeto
2. Criar branch para feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit das alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para branch (`git push origin feature/nova-funcionalidade`)
5. Abrir Pull Request

### Padrões de Código

- Seguir PEP 8 para código Python
- Documentar funções e classes complexas
- Escrever testes para novas funcionalidades
- Manter templates HTML semânticos e organizados

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo LICENSE para mais informações.

## Suporte

Para reportar bugs ou solicitar funcionalidades, abra uma issue no repositório.

## Autores

Desenvolvimento inicial e manutenção do projeto.

## Status do Projeto

Em desenvolvimento ativo.

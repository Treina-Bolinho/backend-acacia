
## Sem docker com virtual env - lista de comandos
    Anotação passo a passo (flavio)

#### Instalar python: 
    sudo apt-get install python3

#### Criar uma virtual ENV:
    python3 -m venv myvenv
    
    se nao der certo
    sudo apt-get install python3.7-venv
    python3 -m venv myvenv

#### Ativar venv:
    source myvenv/bin/activate

#### Com a virtual env ativada:
    
    - instalar Django e DjangoRestFramework 
        >> pip instal django
        >> pip install djangorestframework
    
    - registrar o aplicatico rest_framework  em settings.py -> INSTALLED_APPS
    
    - Criar novo projeto django com nome acacia_api: 
        >> django-admin startproject acacia_api .


    - Sincronize o banco de dados pela primeira vez:
       >> python manage.py makemigrations

    - Criar superusuario:
       >> python manage.py createsuperuser
            admim: admim 
            email address: teste@teste.com.br   
            senha: 123456

    - Criar APIs (na raiz do projeto (SRC))
        >> python manage.py startapp nome API 
      
    - No diretorio de cada API criar novo pacote python (nome api).
        Dentro do pacote/diretorio (api) cria files (viewsets.py, serializers.py)
        
    - Incluir novo API em settings.py -> INSTALLED_APPS
    -> Criar os models com seus atributos (models.py)

                   
    -> Registrar model no admin (admin.py) 
            from.models import core
            admin.site.register(Atracao)
        
    detro de core criar novo pacote python (nome api).
    dentro de api cria files (viewsets.py, serializers.py) 
   
    
    depois de criar a outros pacotes de API
        Importar a as models e fazer os relacionamentos
        
    Fluxo de trabalho 
       >> python manage.py makemigrations
       >> python manage.py migrate
       >> python manage.py runserver
       
       
 -----------------------------------------------------------------      
    #### **Automatizar a construção da API?**
    
    Utilizamos o projeto drf_generators com modificações para funcionar nas versões Django 2.x e DRF 3.9.
    
    Este projeto gera todas as Views, Serializers e as rotas (URLs) para a API a partir do Models.py do Django.
    
    1 — Instalação
    
    pip install drf-generators
    
    2 — Incluir o rest_framework e o drf_generators no settings.py
    
    INSTALLED_APPS = [
     ‘django.contrib.admin’,
     ‘django.contrib.auth’,
     ‘django.contrib.contenttypes’,
     ‘django.contrib.sessions’,
     ‘django.contrib.messages’,
     ‘django.contrib.staticfiles’,
     ‘projeto’,
     ‘rest_framework’,
     ‘drf_generators’,
    ]
    
    3— Executar o comando para a criação das Views, Serializers e URLs:
    
    python .\manage.py generate projeto
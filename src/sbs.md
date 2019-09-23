
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

    após a instalar e ativar a virtual env o 
    comando pip já vai estar ativo.

#### Com a virtual env ativada:
    
    instalar Django e DjangoRestFramework 
        - pip instal django
        - pip install djangorestframework
    
        - Criar novo projeto django com nome acacia_api: 
        django-admin startproject acacia_api .

    fluxo de trabalho 
    
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py runserver


    Criar superusuario:
        python manage.py createsuperuser
        admim: admim 
        email address: teste@teste.com.br   
        senha: 123456

    - Criar api (dentro da pasta do projeto)
        python manage.py startapp nome API 
      
    - Na pasta de cada API criar novo pacote python (nome api).
        Dentro do pacote cria files (viewsets.py, serializers.py)
        
    Adicionar API em INSTALLED_APPS em settings.py
      * core:
       -> criar os models com seus atributos (models.py)
            class PontoTuristico(models.Model):
                nome = models.CharField(max_length=150)
                descricao = models.TextField()
                aprovado = models.BooleanField(default=False)

                 def __str__(self):
                    return self.nome
                    
       registrar model no admin (admin.py) 
            from.models import core
            admin.site.register(Atracao)
        
       detro de core criar novo pacote python (nome api).
       dentro de api cria files (viewsets.py, serializers.py) 
   
    
    depois de criar a outros pacotes de API
        Importar a as models e fazer os relacionamentos
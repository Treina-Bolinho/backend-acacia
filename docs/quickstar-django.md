# Create the project directory
    mkdir tutorial
    cd tutorial

## Create a virtual environment to isolate our package dependencies locally
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

## Install Django and Django REST framework into the virtual environment
    pip install django
    pip install djangorestframework

## Set up a new project with a single application
    django-admin startproject tutorial .  # Note the trailing '.' character
    cd tutorial
    django-admin startapp quickstart
    cd ..

# Serializers
    First up we're going to define some serializers. Let's create a new module named tutorial/quickstart/serializers.py that we'll use for our data representations.
    from django.contrib.auth.models import User, Group
    from rest_framework import serializers


    class UserSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = User
            fields = ['url', 'username', 'email', 'groups']


    class GroupSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Group
            fields = ['url', 'name']
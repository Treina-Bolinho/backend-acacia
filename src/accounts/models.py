from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(('Nome'), max_length=30)
    last_name = models.CharField(('Sobrenome'), max_length=30)
    cpf = models.CharField(('CPF'), max_length=11, blank=True, null=True, unique=True,)
    birth_date = models.DateField(('Data de Nascimento'), null=True, blank=True)
    email = models.EmailField(('Email'), blank=True)
    cel_phone = PhoneField(('Telefone Celular'), blank=True, help_text='Deu ruim')
    res_phone = PhoneField(('Telefone Residencial'), blank=True, help_text='Deu ruim denovo')
    speaks_french = models.BooleanField(('Fala Frances'), default=False)
    speaks_english = models.BooleanField(('Fala Ingles'), default=False)
    bio = models.TextField(('Bio'), max_length=500, blank=True)
    photo = models.ImageField(('Selecione uma Foto do seu computador'), upload_to='pictures_users', blank=True)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



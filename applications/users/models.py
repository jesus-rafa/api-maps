from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, Group,
                                        PermissionsMixin)
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    names = models.CharField('Nombres', max_length=100)
    last_names = models.CharField('Apellidos', max_length=100)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              blank=True,
                              null=True)
    date_birth = models.DateField('Fecha de nacimiento', blank=True, null=True)
    avatar = models.ImageField(
        'Avatar',
        blank=True,
        null=True,
        upload_to='users',
    )
    telefono = models.CharField('Telefono',
                                max_length=10,
                                blank=True,
                                null=True)
    ext = models.CharField('Ext', max_length=5, blank=True, null=True)

    #
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.username = self.email.split('@')[0]
        super(User, self).save(*args, **kwargs)

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.names + ' ' + self.last_names

    def get_initials(self):
        return self.names[:1].upper() + self.last_names[:1].upper()


class Plantilla(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='plantilla')
    orientacion = models.IntegerField('Orientacion', default=0)
    barra = models.IntegerField('Barra', default=0)
    menu = models.IntegerField('Menu', default=0)

    class Meta:
        verbose_name = 'Plantilla'
        verbose_name_plural = 'Plantilla'
        ordering = ['user']

    def __str__(self):
        return str(self.user)


class Urls(models.Model):
    url = models.CharField('Urls', max_length=100)
    icono = models.CharField('Icono', max_length=100, blank=True, null=True)
    nombre = models.CharField('Nombre', max_length=100, blank=True, null=True)
    tags = models.CharField('Tags', max_length=200, blank=True, null=True)
    padre = models.ForeignKey('self',
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE,
                              related_name="hijos")
    sort = models.IntegerField('Sort', blank=True, null=True)
    nivel = models.IntegerField('Nivel', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Urls'
        verbose_name_plural = 'Urls'
        ordering = ['sort']

    def __str__(self):
        return self.nombre


class Accesos(models.Model):
    perfil = models.ForeignKey(Group, on_delete=models.CASCADE)
    urls = models.ManyToManyField(Urls, blank=True, related_name='get_urls')

    class Meta:
        verbose_name = 'Accesos'
        verbose_name_plural = 'Accesos'
        ordering = ['perfil']

    def __str__(self):
        return str(self.perfil)

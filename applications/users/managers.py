from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.db.models import Count


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, username, names, last_names, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            username=username,
            names=names,
            last_names=last_names,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, username, names, last_names, password=None, **extra_fields):
        return self._create_user(email, username, names, last_names, password, True, False, True, **extra_fields)

    def create_superuser(self, email, username, names='', last_names='', password=None, **extra_fields):
        return self._create_user(email, username, names, last_names, password, True, True, True, **extra_fields)

    def usuarios_sistema(self):
        return self.filter(
            is_superuser=False
        ).order_by('-last_login')

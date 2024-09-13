
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .fabricante import Fabricante
from .produto import Produto
from .categoria import Categoria

PERFIL = (
    (1, 'Admin'),
    (2, 'Usuario')
)

from .usuario import Usuario


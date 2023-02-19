from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MinValueValidator


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'cliente'),
        (2, 'helper'),
        (3, 'atendente'),
        (4, 'gerente'),
        (5, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)
    endereco = models.CharField(verbose_name='Endereço', max_length=100, null=True, blank=True)
    telefone = models.CharField(verbose_name='Telefone(Com DDD)', max_length=11, validators=[
        MinLengthValidator(11)
    ], blank=True)
    def __str__(self) -> str:
        return self.username


class Servico(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    
    preco = models.DecimalField(verbose_name='Preço', max_digits=6, decimal_places=2, default=0, validators=[
            MinValueValidator(Decimal('0'))
        ])

    disp = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.nome

class Pagamento(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    def __str__(self) -> str:
        return self.nome

class Situacao(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    def __str__(self) -> str:
        return self.nome

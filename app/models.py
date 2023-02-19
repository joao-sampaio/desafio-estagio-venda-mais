from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.utils.timezone import now
from datetime import date, datetime
from django.core.exceptions import ValidationError

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

class Atendimento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, verbose_name='Serviço', null=True)
    desconto = models.PositiveIntegerField(default=0, verbose_name='Desconto(%)', validators=[
            MaxValueValidator(10)
        ]
    )
    valor_pago = models.DecimalField(verbose_name='Valor Pago', max_digits=7, decimal_places=2)#editable=False,
    forma_de_pag = models.ForeignKey(Pagamento, on_delete=models.SET_NULL, verbose_name='Forma de Pagamento', null=True)
    data_de_cadastro = models.DateTimeField(default=now, editable=False)
    data_servico = models.DateTimeField(default=now, verbose_name='Data e Hora do Serviço')
    situacao = models.ForeignKey(Situacao, to_field='nome', default='Pendente', on_delete=models.SET_NULL, verbose_name='Situação', null=True)
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='cliente', null=True, blank=True)
    atendente = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='atendente', null=True, blank=True)
    helper = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='helper', null=True, blank=True)
    def __str__(self) -> str:
        return f'{self.servico.nome} para {self.cliente.username} em {self.data_servico.strftime(r"%d-%m-%Y %H:%M:%S")}'
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        d = date.today()
        today = datetime(d.year, d.month, d.day)
        if self.data_servico < today:
            raise ValidationError("Selecione uma data futura")
        else:
            self.valor_pago = Decimal((self.servico.preco*(100 - self.desconto))/100)
            return super().save(force_insert, force_update, using, update_fields)
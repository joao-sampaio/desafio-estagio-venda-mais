# Generated by Django 4.1.7 on 2023-02-18 23:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_pagamento_servico_situacao"),
    ]

    operations = [
        migrations.CreateModel(
            name="Atendimento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "desconto",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(10)],
                        verbose_name="Desconto(%)",
                    ),
                ),
                (
                    "valor_pago",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="Valor Pago"
                    ),
                ),
                (
                    "data_de_cadastro",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "data_servico",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Data e Hora do Serviço",
                    ),
                ),
                (
                    "atendente",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="atendente",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="cliente",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "forma_de_pag",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.pagamento",
                        verbose_name="Forma de Pagamento",
                    ),
                ),
                (
                    "helper",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="helper",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "servico",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.servico",
                        verbose_name="Serviço",
                    ),
                ),
                (
                    "situacao",
                    models.ForeignKey(
                        default="Pendente",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.situacao",
                        to_field="nome",
                        verbose_name="Situação",
                    ),
                ),
            ],
        ),
    ]
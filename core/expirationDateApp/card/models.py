from django.db import models
from expirationDateApp.client.models import Client
from django.utils.translation import ugettext_lazy as _
import datetime

YEAR_CHOICES = []
for r in range((datetime.datetime.now().year+1), (datetime.datetime.now().year+10)):
    YEAR_CHOICES.append((r,r))

MONTH_CHOICES=((1, "Janeiro"), (2, "Fevereiro"), (3, "Março"), (4, "Abril"), (5, "Maio"), (6, "Junho"),
               (7, "Julho"), (8, "Agosto"), (9, "Setembro"), (10, "Outubro"), (11, "Novembro"), (12, "Dezembro"))


class Card(models.Model):
    client_id = models.ForeignKey(
        Client,
        verbose_name=_('Client'),
        on_delete=models.CASCADE,
        db_column='cliente',
        blank=True,
        null=True
    )

    card_holder = models.CharField(
        verbose_name=_('card_holder'),
        max_length=50,
        db_column='nome_cartao'
    )

    card_number = models.CharField(
        verbose_name=_('card_number'),
        max_length=16,
        db_column='num_cartao'
    )

    month = models.IntegerField(
        verbose_name=_('Month'),
        choices=MONTH_CHOICES,
        db_column='mes_exp'
    )

    year = models.IntegerField(
        verbose_name=_('Year'),
        choices=YEAR_CHOICES,
        db_column='ano_exp'
    )

    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=False,
        db_column='ativo'
    )

    class Meta:
        verbose_name = _('Card')
        verbose_name_plural = _('Cards')
        db_table = 'cartoes'

    def __str__(self):
        return '{} - {}'.format(self.card_holder, self.card_number)

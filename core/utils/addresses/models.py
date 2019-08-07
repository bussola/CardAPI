from django.db import models
from django.utils.translation import ugettext_lazy as _


class AddressAbstract(models.Model):

    number = models.IntegerField(
        verbose_name=_("Address Number"),
        db_column="num_logradouro",
        default=''
    )
    address = models.CharField(
        verbose_name=_("Address"),
        max_length=40,
        db_column="logradouro",
        default=''
    )
    neighborhood = models.CharField(
        verbose_name=_("Neighborhood"),
        max_length=15,
        db_column="bairro",
        default=''
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=15,
        db_column="cidade",
        default=''
    )
    uf = models.CharField(
        verbose_name=_("UF"),
        max_length=2,
        db_column="uf",
        default=''
    )
    cep = models.CharField(
        verbose_name=_("CEP"),
        max_length=8,
        db_column="cep",
        default=''
    )

    class Meta:
        abstract = True

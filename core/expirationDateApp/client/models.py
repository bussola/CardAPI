from django.db import models
from utils.addresses.models import AddressAbstract


class Client(AddressAbstract):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

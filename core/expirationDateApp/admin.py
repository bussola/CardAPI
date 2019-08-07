from django.contrib import admin
from expirationDateApp.card.models import Card
from expirationDateApp.client.models import Client

admin.site.register(Client)
admin.site.register(Card)

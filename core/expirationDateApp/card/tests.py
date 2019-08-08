from django.test import TestCase
from expirationDateApp.card.models import Card
from expirationDateApp.client.models import Client
from mixer.backend.django import mixer
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST


class CardTestCase(TestCase):
    def setUp(self):
        Client.objects.create(
            name="Joao Jose Silva",
            cep="15091220",
            uf="SP",
            city="Ribeirao Preto",
            neighborhood="Jd Italia",
            address="Rua das avenidas",
            number="23"
        )
        cliente = Client.objects.get(name="Joao Jose Silva")

        Card.objects.create(
            client_id=cliente,
            card_holder="Joao J Silva",
            card_number=1234567890123456,
            month="12",
            year="2011",
            is_active=True
        )

        cartoes = mixer.cycle(5).blend('expirationDateApp.Card')
        print(cartoes)

    def test_card_is_active(self):
        card = Card.objects.get(card_number=1234567890123456)
        self.assertEqual(card.is_active, True)


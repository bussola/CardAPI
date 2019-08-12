from django.test import TestCase
from rest_framework.utils import json
from expirationDateApp.card.models import Card
from expirationDateApp.card.serializers import CardSerializer
from expirationDateApp.client.models import Client
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, \
    HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from rest_framework.test import APIClient
from expirationDateApp.client.serializers import ClientSerializer


class CardGetTest(TestCase):
    def setUp(self):
        self.uri = '/valid-thru/'
        self.client = APIClient()

        cliente = Client.objects.create(
            id=1, name='Joao1',
            number=1,
            address='Rua 1',
            neighborhood='Bairro 1',
            city='Cidade 1',
            uf='SP',
            cep='11999888'
        )
        Card.objects.create(
            id=1, client_id=cliente,
            card_holder="Joao1",
            card_number='1111222233334444',
            month='12',
            year='2022',
            is_active='True'
        )
        Card.objects.create(
            id=2, client_id=cliente,
            card_holder="Joao2",
            card_number='1111222233334444',
            month='12',
            year='2022',
            is_active='False'
        )

    def test_get_all_cards(self):
        response = self.client.get(self.uri)
        cartao = Card.objects.all()
        serializer = CardSerializer(cartao, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_get_valid_single_card(self):
        response = self.client.get(self.uri + '1/')
        cartao = Card.objects.get(pk=1)
        serializer = CardSerializer(cartao)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_get_invalid_single_card(self):
        response = self.client.get(self.uri + '999/')
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)


class CardPostTest(TestCase):
    def setUp(self):
        Client.objects.create(
            id=1, name='Joao1',
            number=1,
            address='Rua 1',
            neighborhood='Bairro 1',
            city='Cidade 1',
            uf='SP',
            cep='11999888'
        )
        self.uri = '/valid-thru/'
        self.client = APIClient()
        self.valid_payload = {
            'client_id': 1,
            'card_holder': "Joao 1",
            'card_number': '1111222233334444',
            'month': '11',
            'year': '2020',
            'is_active': 'True'
        }
        self.invalid_payload = {
            'client_id': 'cliente',
            'card_holder': "Joao 1",
            'card_number': '1111222233334444',
            'month': '11',
            'year': '2020',
            'is_active': 'True'
        }

    def test_create_valid_card(self):
        response = self.client.post(
            self.uri,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_create_invalid_card(self):
        response = self.client.post(
            self.uri,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)


class CardPutTest(TestCase):
    def setUp(self):
        self.uri = '/valid-thru/'
        self.client = APIClient()
        cliente1 = Client.objects.create(
            id=1, name='Joao1',
            number=1,
            address='Rua 1',
            neighborhood='Bairro 1',
            city='Cidade 1',
            uf='SP',
            cep='11999888'
        )
        Card.objects.create(
            id=1, client_id=cliente1,
            card_holder="Joao1",
            card_number='1111222233334444',
            month='12',
            year='2022',
            is_active='True'
        )

        self.valid_payload = {
            'client_id': 1,
            'card_holder': "Joao 1",
            'card_number': '1111222233334444',
            'month': '11',
            'year': '2020',
            'is_active': 'True'
        }
        self.invalid_payload = {
            'client_id': 'cliente',
            'card_holder': "Joao 1",
            'card_number': '1111222233334444',
            'month': '11',
            'year': '2020',
            'is_active': 'True'
        }

    def test_valid_update_card(self):
        response = self.client.put(
            (self.uri + '1/'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_invalid_update_card(self):
        response = self.client.put(
            (self.uri + '1/'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)


class CardDeleteTest(TestCase):
    def setUp(self):
        self.uri = '/valid-thru/'
        self.client = APIClient()
        cliente1 = Client.objects.create(
            id=1, name='Joao1',
            number=1,
            address='Rua 1',
            neighborhood='Bairro 1',
            city='Cidade 1',
            uf='SP',
            cep='11999888'
        )
        Card.objects.create(
            id=1, client_id=cliente1,
            card_holder="Joao1",
            card_number='1111222233334444',
            month='12',
            year='2022',
            is_active='True'
        )
        Card.objects.create(
            id=2, client_id=cliente1,
            card_holder="Joao2",
            card_number='1111222233334444',
            month='12',
            year='2022',
            is_active='False'
        )

    def test_valid_delete_card(self):
        response = self.client.delete(
            (self.uri + '1/')
        )
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_invalid_delete_card(self):
        response = self.client.delete(
            (self.uri + '999/'),)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_valid_thru(self):
        response = self.client.get(
            (self.uri + '?month=12&year=2022'),)
        print(response)
        for r in response:
            if "Joao1" in str(r):
                self.assertEqual(HTTP_200_OK, HTTP_200_OK)
            else:
                self.assertEqual(HTTP_200_OK, HTTP_404_NOT_FOUND)
            if "Joao2" in str(r):
                self.assertEqual(HTTP_200_OK, HTTP_404_NOT_FOUND)
            else:
                self.assertEqual(HTTP_200_OK, HTTP_200_OK)

from django.test import TestCase
from rest_framework.utils import json
from expirationDateApp.card.models import Card
from expirationDateApp.card.serializers import CardSerializer
from expirationDateApp.client.models import Client
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, \
    HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from rest_framework.test import APIClient
from expirationDateApp.client.serializers import ClientSerializer


class ClientsGetTest(TestCase):
    def setUp(self):
        self.uri = '/clients/'
        self.client = APIClient()

        Client.objects.create(
            id=1, name='Joao1',
            number=1,
            address='Rua 1',
            neighborhood='Bairro 1',
            city='Cidade 1',
            uf='SP',
            cep='11999888'
        )
        Client.objects.create(
            id=2, name='Joao1',
            number=1,
            address='Rua 1',
            neighborhood='Bairro 1',
            city='Cidade 1',
            uf='SP',
            cep='11999888'
        )

    def test_get_all_clients(self):
        # get API response
        response = self.client.get(self.uri)
        # get data from db
        cliente = Client.objects.all()
        serializer = ClientSerializer(cliente, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_get_valid_single_client(self):
        response = self.client.get(self.uri + '1/')
        cliente = Client.objects.get(pk=1)
        serializer = ClientSerializer(cliente)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_get_invalid_single_client(self):
        response = self.client.get(self.uri + '999/')
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)


class ClientPostTest(TestCase):
    def setUp(self):
        self.uri = '/clients/'
        self.client = APIClient()
        self.valid_payload = {
            'name': 'Joao',
            'number': 4,
            'address': 'Rua da ruas',
            'neighborhood': 'Bairro X',
            'city': 'Cidade',
            'uf': 'SP',
            'cep': '14888000'
        }
        self.invalid_payload = {
            'name': 1,
            'number': "quatro",
            'address': 'Rua da ruas',
            'neighborhood': 'Bairro X',
            'city': 'Cidade',
            'uf': 'SP',
            'cep': '14888000'
        }

    def test_create_valid_client(self):
        response = self.client.post(
            self.uri,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_create_invalid_client(self):
        response = self.client.post(
            self.uri,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)


class ClientPutTest(TestCase):
    def setUp(self):
        self.uri = '/clients/'
        self.client = APIClient()
        self.cliente1 = Client.objects.create(
            id=1, name='Joao1',
            number=1,
            address='Rua 1',
            neighborhood='Bairro 1',
            city='Cidade 1',
            uf='SP',
            cep='11999888'
        )

        self.valid_payload = {
            'name': 'Joao',
            'number': 4,
            'address': 'Rua da ruas',
            'neighborhood': 'Bairro X',
            'city': 'Cidade',
            'uf': 'SP',
            'cep': '14888000'
        }
        self.invalid_payload = {
            'name': 1,
            'number': "quatro",
            'address': 'Rua da ruas',
            'neighborhood': 'Bairro X',
            'city': 'Cidade',
            'uf': 'SP',
            'cep': '14888000'
        }

    def test_valid_update_client(self):
        response = self.client.put(
            (self.uri + '1/'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_invalid_update_client(self):
        response = self.client.put(
            (self.uri + '1/'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)


class ClientDeleteTest(TestCase):
    def setUp(self):
        self.uri = '/clients/'
        self.client = APIClient()
        self.cliente1 = Client.objects.create(
            id=1, name='Joao1',
            number=1,
            address='Rua 1',
            neighborhood='Bairro 1',
            city='Cidade 1',
            uf='SP',
            cep='11999888'
        )

    def test_valid_delete_client(self):
        response = self.client.delete(
            (self.uri + '1/')
        )
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_invalid_delete_client(self):
        response = self.client.delete(
            (self.uri + '999/'),)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
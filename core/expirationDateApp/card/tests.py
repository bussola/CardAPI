from django.test import TestCase
from expirationDateApp.card.models import Card
from expirationDateApp.card.serializers import CardSerializer
from expirationDateApp.client import viewsets
from expirationDateApp.client.models import Client
from mixer.backend.django import mixer
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from expirationDateApp.client.serializers import ClientSerializer


class ClientsTest(TestCase):

    def setUp(self):
        self.uri = '/clients/'
        self.client = APIClient()
        Client.objects.create(
            name='Joao1', number=1, address='Rua 1', neighborhood='Bairro 1', city='Cidade 1', uf='SP', cep='11999888')
        Client.objects.create(
            name='Joao2', number=2, address='Rua 2', neighborhood='Bairro 2', city='Cidade 2', uf='SP', cep='11999887')
        Client.objects.create(
            name='Joao3', number=3, address='Rua 3', neighborhood='Bairro 3', city='Cidade 3', uf='SP', cep='11999886')
        Client.objects.create(
            name='Joao4', number=4, address='Rua 4', neighborhood='Bairro 4', city='Cidade 4', uf='SP', cep='11999885')

    def test_get_all_clients(self):
        # get API response
        response = self.client.get(self.uri)
        # get data from db
        cliente = Client.objects.all()
        serializer = ClientSerializer(cliente, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_get_valid_single_puppy(self):
        response = self.client.get(self.uri)
        cliente = Client.objects.get(pk=1)
        serializer = ClientSerializer(cliente)
        self.assertEqual(response.data[0], serializer.data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_get_invalid_single_puppy(self):
        response = self.client.get(self.uri)
        try:
            existe = response.data[10]
        except Exception as e:
            existe = None
            print(e)
        # print("Negocio: " + str(naoexiste))
        self.assertEqual(existe, None)

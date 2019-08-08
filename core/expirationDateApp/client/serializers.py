from rest_framework.serializers import ModelSerializer
from expirationDateApp.client.models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'cep', 'uf', 'city', 'neighborhood', 'address', 'number')

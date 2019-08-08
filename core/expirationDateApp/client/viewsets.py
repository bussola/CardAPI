from rest_framework.viewsets import ModelViewSet
from expirationDateApp.client.models import Client
from expirationDateApp.client.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
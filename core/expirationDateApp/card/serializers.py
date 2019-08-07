from rest_framework.serializers import ModelSerializer
from expirationDateApp.card.models import Card


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('client_id', 'card_holder', 'card_number', 'month', 'year', 'is_active')

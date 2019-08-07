from rest_framework.serializers import ModelSerializer
from expirationDateApp.card.models import Card

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer, DecimalField, CharField, DateField, IntegerField
from rest_framework.exceptions import ValidationError


class CardSerializer(ModelSerializer):
    card_number = SerializerMethodField()

    def get_card_number(self, obj):
        envrypt_card_number = obj.card_number
        envrypt_card_number = envrypt_card_number[-4:].rjust(len(envrypt_card_number), "*")
        return envrypt_card_number

    class Meta:

        model = Card
        fields = ('client_id', 'card_holder', 'card_number', 'month', 'year', 'is_active')

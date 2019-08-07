from expirationDateApp.card.models import Card
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer


class CardSerializer(ModelSerializer):
    card_number = SerializerMethodField()

    def get_card_number(self, obj):
        encrypt_card_number = obj.card_number
        encrypt_card_number = encrypt_card_number[-4:].rjust(len(encrypt_card_number), "*")
        return encrypt_card_number

    class Meta:
        model = Card
        fields = ('client_id', 'card_holder', 'card_number', 'month', 'year', 'is_active')

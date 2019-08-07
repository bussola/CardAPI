from rest_framework.viewsets import ModelViewSet
from expirationDateApp.card.models import Card
from expirationDateApp.card.serializers import CardSerializer


class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = Card.objects.all()
        year = self.request.query_params.get('year', None)
        month = self.request.query_params.get('month', None)
        if month is not None and year is not None:
            queryset = queryset.filter(month=month, year=year, is_active=True)
        return queryset

import csv
from expirationDateApp.card.models import Card
from expirationDateApp.client.models import Client


def insert_cards():
    arquivo = "utils/csv/cards.csv"
    with open(arquivo) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Card.objects.get_or_create(
                client_id=Client.objects.get(id=row[0]),
                card_holder=row[1],
                card_number=row[2],
                month=row[3],
                year=row[4],
                is_active=row[5],
            )

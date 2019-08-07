import csv
from expirationDateApp.client.models import Client


def insert_clients():
    arquivo = "utils/csv/clients.csv"
    with open(arquivo) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Client.objects.get_or_create(
                id=row[0],
                name=row[1],
                cep=row[2],
                uf=row[3],
                city=row[4],
                neighborhood=row[5],
                address=row[6],
                number=row[7],
            )

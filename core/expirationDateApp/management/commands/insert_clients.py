from django.core.management import BaseCommand
from utils.csv.importClients import insert_clients


class Command(BaseCommand):
    help = "Popula tabela de Clientes"

    def handle(self, *args, **options):
        insert_clients()

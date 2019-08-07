from django.core.management import BaseCommand
from utils.csv.importCards import insert_cards


class Command(BaseCommand):
    help = "Popula tabela de Cartoes"

    def handle(self, *args, **options):
        insert_cards()

import json
from django.core.management.base import BaseCommand
from models import Product
# O'zingizning modelingizni import qiling


class Command(BaseCommand):
    help = 'Export data from Watches table to JSON file'

    def handle(self, *args, **kwargs):
        # Ma'lumotlarni olish
        data = Product.objects.all().values()  # Barcha ma'lumotlarni olish

        # JSON formatida saqlash
        with open('watches_data.json', 'w') as f:
            json.dump(list(data), f, indent=4)

        self.stdout.write(self.style.SUCCESS('Data exported successfully to watches_data.json'))


from django.core.management import BaseCommand
from catalog.models import  Category
class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {"name":"мясо", "description":"hold"}, {"name":"рыба", "description":"hold"}
        ]


        category_for_create = []
        for item in category_list:
            category_for_create.append(Category(**item))

        Category.objects.bulk_create(category_for_create)


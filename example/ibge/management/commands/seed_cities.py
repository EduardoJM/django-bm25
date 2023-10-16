import requests
import json
from django.core.management.base import BaseCommand
from example.ibge.models import City


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(
            "https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/json/municipios.json"
        )
        json_data = json.loads(response.text)
        data = json_data["data"]
        for city in data:
            state = city["Uf"]
            code = city["Codigo"]
            name = city["Nome"]
            City.objects.create(state=state, code=code, name=name)

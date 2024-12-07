# tasks.py
from celery import shared_task
import requests
from .models import Stocks


@shared_task
def fetch_data_from_api():
    api_url = 'https://12af-14-97-224-214.ngrok-free.app/index'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        # stock_id = models.CharField(max_length=100, null=False)
        # name = models.CharField(max_length=100)
        # group = models.CharField(max_length=100)
        # date = models.CharField(max_length=100)
        # value = models.CharField(max_length=100)
        # "id":"VLCC","name":"index1","group":"bulk","date":"2024-12-06","value":100
        for item in data:
            Stocks.objects.create(
                stock_id=item['id'],
                name=item['name'],
                group=item['group'],
                date=item['item'],
                value=item['value']
            )

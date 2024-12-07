from django.db import models

# Create your models here.



class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    is_admin = models.BooleanField(null=True)


class Stocks(models.Model):
    # "id":"VLCC","name":"index1","group":"bulk","date":"2024-12-06","value":100
    stock_id = models.CharField(max_length=100,null=False)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    value = models.CharField(max_length=100)




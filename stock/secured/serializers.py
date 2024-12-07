from rest_framework import serializers
from .models import User,Stocks


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id',
                  'email',
                  'password',
                  'group',)

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stocks
        fields = ('stock_id',
                  'name',
                  'group',
                  'date',
                  'value',)

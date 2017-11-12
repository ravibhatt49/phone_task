from rest_framework import serializers
from .models import *

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields = ('id', 'model_name', 'owner_name', 'purchase_price', 'sell_price', 'received_date', 'description', 'profit')


class PartySerializers(serializers.ModelSerializer):
    class Meta:
        model=Party
        fields = ('id', 'name', 'debit_amount', 'credit_amount')
        
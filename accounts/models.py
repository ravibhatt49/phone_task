from django.db import models

# Create your models here.
class Task(models.Model):
    model_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=30)
    purchase_price = models.IntegerField(blank=True)
    sell_price = models.IntegerField(blank=True)
    received_date = models.DateField(blank=True)
    description = models.CharField(max_length=300)

    @property
    def profit(self):
        try:
            purchase_price = self.purchase_price
        except Exception as e:
            purchase_price = 0
        try:
            sell_price = self.sell_price
        except Exception as e:
            sell_price = 0
        profit = sell_price - purchase_price
        return profit


class Party(models.Model):
    name = models.CharField(max_length=50)
    debit_amount = models.IntegerField(null=True, blank=True)
    credit_amount = models.IntegerField(null=True, blank=True)

from django.db import models

# Create your models here.

class BinanceBot(models.Model):
    balance = models.FloatField()
    trades = models.IntegerField()
    date_created = models.DateTimeField(null=True, auto_now_add=True)


class HistoricalData(models.Model):
    symbol = models.CharField(max_length=20)
    timestamp = models.DateTimeField(unique=True)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.symbol

    

class CryptoAsset(models.Model):
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    market_cap = models.FloatField()
    price = models.FloatField()
    volume = models.FloatField()
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Stock(models.Model):
    ticker = models.CharField(max_length = 4, unique = True)
    

class History(models.Model):
    pass

class Transaction(models.Model):
    date = models.DateTimeField(editable = False, auto_now_add = True)
    stock = models.ForeignKey(Stock, blank = False, null = False)
    quantity = models.PositiveIntegerField( blank = False, null = False)
    history = models.ForeignKey(History, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 9, 
            decimal_places = 2,
            blank = False,
            null = False,
            validators = MinValueValidator(Decimal('0.01')),
        )

    @property
    def total(self):
        return self.price * self.quantity

    class Meta:
        abstract = True

class SellTransaction(Transaction):
    def __str__(self):
        return "{0} units of {1} sold at {2}/share for a total of {3}".format \
            (self.quantity, self.stock, self.price,
            self.quantity * self.price
            )


class BuyTransaction(Transaction):
    def __str__(self):
        return "{0} units of {1} bought at {2}/share for a total of {3}".format \
            (self.quantity, self.stock, self.price,
            self.quantity * self.price
            )

class Account(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE, editable = False)
  balance = models.PositiveIntegerField()
  # each account has a history of transactions, deposits
  history = models.OneToOneField(History, on_delete = models.CASCADE)



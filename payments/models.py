# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart
from books.models import Book

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=True)
    cart = models.ForeignKey('cart.Cart', on_delete=models.SET_NULL, null=True, default=True)
    amount = models.IntegerField(null=True, blank=True)
    credit_card = models.IntegerField(default=True, help_text="Credit Card Details")
    charge_id = models.CharField(max_length=200, help_text="Charge ID")
    card_id = models.CharField(max_length=200,default=True, help_text="Card ID")
    status = models.CharField(max_length=200,default=True, help_text="Payment Status")



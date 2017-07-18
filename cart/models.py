# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

from books.models import Book,Order


# Create your models here.
class Cart(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.SET_NULL, null=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    order = models.ForeignKey('books.Order', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(help_text="Enter number of Copies" ,null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from books.models import Book,Order


# Create your models here.
class Cart(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.SET_NULL, null=True, default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=True)
    order = models.ForeignKey('books.Order', on_delete=models.CASCADE, null=True, default=True)
    quantity = models.IntegerField(default=True, help_text="Enter number of Copies")
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
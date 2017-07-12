# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cart.models import Cart

# Register your models here.

class CartAdmin(admin.ModelAdmin):
	list_display = ('user', 'book' ,'order', 'quantity', 'total_price')

admin.site.register(Cart, CartAdmin)
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('credit_card', models.IntegerField(default=True, help_text='Credit Card Details')),
                ('charge_id', models.CharField(help_text='Charge ID', max_length=200)),
                ('card_id', models.CharField(default=True, help_text='Card ID', max_length=200)),
                ('status', models.CharField(default=True, help_text='Payment Status', max_length=200)),
                ('cart', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.Cart')),
                ('user', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

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
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('isbn', models.CharField(default=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
                ('summary', models.TextField(default='DEFAULT VALUE', help_text='Enter a brief description of the book', max_length=10000)),
                ('price', models.IntegerField(default=True, help_text='Enter Daily rental Price')),
                ('count', models.IntegerField(default=True, help_text='Enter number of Copies')),
                ('imprint', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, choices=[('n', 'Not Available'), ('a', 'Available')], default='d', help_text='Book availability', max_length=1)),
                ('author', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('credit_card', models.IntegerField(default=True, help_text='Credit Card Details')),
                ('charge_id', models.CharField(default=True, help_text='Charge ID', max_length=200)),
                ('card_id', models.CharField(default=True, help_text='Card ID', max_length=200)),
                ('status', models.CharField(default=True, help_text='Payment Status', max_length=200)),
                ('book', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Book')),
                ('user', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='books.Genre'),
        ),
    ]

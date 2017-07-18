# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User



class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)  

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(
        'ISBN',
        max_length=13, 
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', 
        default=True
    )
    summary = models.TextField(max_length=10000, null=True, blank =True, help_text="Enter a brief description of the book")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    price = models.IntegerField(null=True, help_text="Enter Daily rental Price")
    count = models.IntegerField(null=True, help_text="Enter number of Copies")
    imprint = models.CharField(max_length=200, blank=True, null=True)
    
    LOAN_STATUS = (
        ('n', 'Not Available'),
        ('a', 'Available'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')
    figure = models.ImageField(upload_to='images/',
                               blank=True,
                               null=True,
                               verbose_name=("Figure"))

    def __str__(self):
        return '%s, (%s)' % (self.id, self.title)
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=True)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, default=True)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    credit_card = models.IntegerField(default=True, help_text="Credit Card Details")
    charge_id = models.CharField(max_length=200,default=True, help_text="Charge ID")
    card_id = models.CharField(max_length=200,default=True, help_text="Card ID")
    status = models.CharField(max_length=200,default=True, help_text="Payment Status")


    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])

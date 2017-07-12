# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from books.models import Book, Author, Genre, Order


admin.site.register(Genre)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn')
    list_filter = ('author', 'title')

admin.site.register(Book, BookAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 
    	'book', 
    	'issue_date', 
    	'return_date', 
    	'amount', 
    	'credit_card', 
    	'charge_id', 
    	'card_id', 
    	'status'
    )

admin.site.register(Order, OrderAdmin)

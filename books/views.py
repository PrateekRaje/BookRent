# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from datetime import datetime

from books.models import Book, Author, Genre, Order
import operator


def index(request):
   
    num_books=Book.objects.all().count()
    num_authors=Author.objects.count()  
    
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    
    return render(
        request,
        'index.html',
        context={'num_books':num_books,
            'num_authors':num_authors,
            'num_visits':num_visits
        },
    )
def book_list(request):
    book = Book.objects.all()
    return render(request,'books/book_list.html',{'book_list':book})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/book_detail.html',{'book':book})

def author_list(request):
    author = Author.objects.all()
    return render(request,'books/author_list.html',{'author_list':author})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'books/author_detail.html',{'author':author})

def checkAvailability(request, book_id):
   
    book = Book.objects.get(pk=book_id)
    
    issue_date = request.GET['field1']
    return_date = request.GET['field2']
    # convert string to date object first before compare 
    order = Order.objects.filter(book=book_id)
    issue_date = datetime.strptime(issue_date, "%m/%d/%Y").strftime("%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%m/%d/%Y").strftime("%Y-%m-%d")

    for orders in order:
       
       previous_issue_date = str(orders.issue_date)
       previous_return_date = str(orders.return_date)
       
       print previous_issue_date
       print previous_return_date

       if issue_date >= previous_issue_date and issue_date <= previous_return_date:
           reply = "BOOK NOT AVAILABLE ,BOOK IS ISSUEED FOR THE CHOSEN DATES"
           return HttpResponse({reply})
           break;    
       
       if issue_date <= previous_return_date and issue_date <= previous_return_date:
           reply = "BOOK NOT AVAILABLE ,BOOK IS ISSUEED FOR THE CHOSEN DATES"    
           return HttpResponse({reply})
       
    reply =  "CONTINUE TO RENT"
    return HttpResponse({reply})





                

           



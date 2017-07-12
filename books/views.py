# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.db.models import Q

from datetime import datetime
import operator

from django.contrib.auth.models import User
from .models import Book, Author, Genre, Order

def index(request):
    """
    View function for home page of site."""
    
    num_books=Book.objects.all().count()
    num_instances=Book.objects.all().count()
    num_instances_available=Book.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'num_visits':num_visits},
    )

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    
    
    def get_queryset(self):
        result = super(BookListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains =q) for q in query_list))
            )
                
        return result


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'books/author_list.html'


    def get_queryset(self):
        result = super(AuthorListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(first_name__icontains =q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(last_name__icontains =q) for q in query_list))
            )
                
        return result


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'books/author_detail.html'

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book_details = {'status':book.status,'due_back':book.due_back,'imprint':book.imprint}
    return render(request, 'bookrent/book_detail.html', {'book':book,'book_details':book_details})


class RentListView(generic.ListView):
    model = Order   
    template_name = 'books/rent_list.html'

def rent_list(request, book_id):
    book = Book.objects.get(id= book_id)
    return render(request, 'bookrent/rent_list.html', {'book':book})


class RentDetailView(generic.DetailView):
    model = Order
    template_name = 'books/rent_detail'



def checkAvailability(request, book_id):
    book = Book.objects.get(pk=book_id)
    #order = Order.objects.get(pk=order_id)

    issue_date = request.GET['field1']
    return_date = request.GET['field2']

    order = Order.objects.filter(book=book_id)
    #print order.filter(count > 2)
    issue_date = datetime.strptime(issue_date, "%m/%d/%Y").strftime("%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%m/%d/%Y").strftime("%Y-%m-%d")

    for orders in order:
       
       previous_issue_date = str(orders.issue_date)
       previous_return_date = str(orders.return_date)
       
       print previous_issue_date
       print previous_return_date

       if issue_date >= previous_issue_date and issue_date <= previous_return_date:
           var1 = "BOOK NOT AVAILABLE ,BOOK IS ISSUEED FOR THE CHOSEN DATES"
           return HttpResponse({var1})
           break;    
       
       if issue_date <= previous_return_date and issue_date <= previous_return_date:
           var1 = "BOOK NOT AVAILABLE ,BOOK IS ISSUEED FOR THE CHOSEN DATES"    
           return HttpResponse({var1})
       

    var2 =  "CONTINUE TO RENT"
    return HttpResponse({var2})
           



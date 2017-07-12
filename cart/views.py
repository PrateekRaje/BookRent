# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.models import User

from books.models import Book, Order
from cart.models import Cart


# Create your views here.
def add_to_cart(request, book_id):
   
    print "WORKING!!"
    issue_date = request.GET['field1']
    return_date = request.GET['field2']

    issue_date = datetime.strptime(issue_date, "%m/%d/%Y").strftime("%m-%d-%Y")
    return_date = datetime.strptime(return_date, "%m/%d/%Y").strftime("%m-%d-%Y")
    
    issue_date = datetime.strptime(issue_date, '%m-%d-%Y') 
    return_date = datetime.strptime(return_date, '%m-%d-%Y') 
    
    book = Book.objects.get(pk=book_id)
    user= User.objects.get(pk=request.user.id)

    days = return_date - issue_date
    total_days= days.days
    total_price = total_days * int(book.price)

    Cart.objects.create(user=user, book=book, issue_date=issue_date, return_date=return_date, total_price=total_price)
    var = "Book is added to Cart!!"
    return HttpResponse({var})

def view_cart(request, book_id):

    cart = Cart.objects.filter(user=request.user.id)
    total_amount=0
    for item in cart:
        total_amount= total_amount + item.total_price
        
    total_money = total_amount*100
    return render(request, "cart/cart_detail.html", {'product':cart, 'total_amount': total_amount, 'total_money': total_money})


def booking(request):

    cart = Cart.objects.filter(user=request.user.id)
    user = User.objects.get(pk=request.user.id)
    for items in cart:
        book = Book.objects.get(pk=items.book.id)
        Order.objects.create(book_id= book.id, user= user, issue_date=items.issue_date, return_date=items.return_date, total_price=items.total_price)
    
    count = book.count - 1
    book.count = count
    book.save()

    return HttpResponse("Book is RENTED!!")      
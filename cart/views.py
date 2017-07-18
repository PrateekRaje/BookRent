# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from books.models import Book, Order
from cart.models import Cart


# Create your views here.
@login_required
def add_to_cart(request, book_id):
    # import pdb
    # pdb.set_trace()

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
       
  
    quantity = request.GET['quantity']
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
    total_price = (total_days * int(book.price))* int(quantity)
   
    Cart.objects.create(user=user, book=book, issue_date=issue_date, return_date=return_date, total_price=total_price, quantity=quantity)
    
    reply =  "CONTINUE TO RENT"
    return HttpResponse({reply})
         
@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user.id)
    total_amount=0
    for item in cart:
        total_amount= total_amount + item.total_price
        
    total_money = total_amount*100
    return render(request, "cart/cart_detail.html", {'product':cart, 'total_amount': total_amount, 'total_money': total_money, })

def delete_from_cart(request, items_id):
    Cart.objects.get(id =items_id).delete()    
    return HttpResponseRedirect('/cart/cartview/')
 
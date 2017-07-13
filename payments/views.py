# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse


from django.shortcuts import render
from django.contrib.auth.models import User

from books.models import Book, Order
from cart.models import Cart
from payments.models import Payment


import stripe

stripe.api_key = "sk_test_d4iXJ56imIxwGMKEzQPKz2bY"


# Create your views here.
def pay(request, price):
    
    # import pdb
    # pdb.set_trace()
    user = User.objects.get(pk=request.user.id)

    token = request.POST['stripeToken'] 
    customer = stripe.Customer.create(
        email=user.email,
        source=token,
    )
    charge = stripe.Charge.create(
        amount=price,
        currency="inr",
        customer=customer.id,
    )

    cart = Cart.objects.filter(user=request.user.id)
    user = User.objects.get(pk=request.user.id)
    amount = (charge.amount/100)
    
    for items in cart:
        book = Book.objects.get(pk=items.book.id)
        Order.objects.create(book_id= book.id, 
            user= user,
            issue_date=items.issue_date, 
            return_date=items.return_date,
            amount= amount,
            credit_card= charge.source.last4,
            charge_id=charge.id, 
            card_id=charge.source.id, 
            status=charge.status
        )

    Cart.objects.filter(user=request.user.id).delete()    

    return HttpResponse("PAYMENT WORKING!!")

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import stripe

from books.models import Book, Order
from cart.models import Cart
from payments.models import Payment
from BookRent import settings

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

    # book = Book.objects.get(pk=items.book.id)
    cart = Cart.objects.filter(user=request.user.id)
    user = User.objects.get(pk=request.user.id)
    amount = (charge.amount/100)
    
    for items in cart:
        book = Book.objects.get(pk=items.book.id)
        Order.objects.create(book= items.book, 
            user= user,
            issue_date=items.issue_date, 
            return_date=items.return_date,
            quantity = items.quantity,
            amount= amount,
            credit_card= charge.source.last4,
            charge_id=charge.id, 
            card_id=charge.source.id, 
            status=charge.status
        )

        count = book.count - 1
        book.count = count
        book.save()    

    Cart.objects.filter(user=request.user.id).delete()
    return (sendEmailWithAttach(request))

def sendEmailWithAttach(request):
    subject = "Hello"
    html_content = render_to_string('email.html')
    email_from = settings.EMAIL_HOST_USER
    email_to = ['prateekbhonsale@gmail.com']
    email = EmailMessage(subject, html_content, email_from, email_to)
    email.content_subtype = "html"
    res = email.send()
    
    return HttpResponse("PAYMENT COMPLETED !!!")







# Create your views here.

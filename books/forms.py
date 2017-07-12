from django.contrib.auth import get_user_model
from django import forms

from django.contrib.auth.models import User

class SignupForm(forms.Form):
    fname = forms.CharField(max_length=30, help_text="Enter First Name",)
    lname = forms.CharField(max_length=30, help_text="Enter Last Name",)

    def signup(self, request, user):
        user.fname = self.cleaned_data['fname']
        user.lname = self.cleaned_data['lname']
        user.save()
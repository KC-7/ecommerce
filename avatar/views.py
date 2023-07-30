from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView
from django.urls import reverse_lazy
from .generate import generate_and_save_punk_for_user
from django.contrib.auth.models import User


class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)  # Save the user and get the response
        user = self.user  # The user object is accessible after the form is saved
        print('Attempting to create punk')
        generate_and_save_punk_for_user(user, self.request)
        print('Successfully generated punk')
        return response


# class CustomSignupView(SignupView):
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         generate_and_save_punk_for_user(self.request)
#         return response

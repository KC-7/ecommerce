from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView
from django.urls import reverse_lazy
from .generate import generate_and_save_punk_for_user
from django.contrib.auth.models import User
from .models import Avatar


class CustomSignupView(SignupView):
    """ Creates custom punk avatar when creating new accounts """
    def form_valid(self, form):
        response = super().form_valid(form)  # Save the user and get the response
        user = self.user  # The user object is accessible after the form is saved
        print('Attempting to create punk')
        generate_and_save_punk_for_user(user, self.request)
        print('Successfully generated punk')
        return response


@login_required
def avatar_detail(request):
    """ Displays Punk and Stats """
    user = request.user
    try:
        avatar = Avatar.objects.get(user=user)
    except Avatar.DoesNotExist:
        avatar = None

    template = 'avatar/avatar_detail.html'
    context = {
        'avatar': avatar,
    }

    return render(request, template, context)

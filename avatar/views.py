from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView
from .generate import generate_and_save_punk_for_user
from .models import Avatar


class CustomSignupView(SignupView):
    """ Creates custom punk avatar when creating new accounts """
    def form_valid(self, form):
        # Save the user and get the response
        response = super().form_valid(form)
        # The user object is accessible after the form is saved
        user = self.user
        # Generate the custom punk for user
        generate_and_save_punk_for_user(user, self.request)
        return response


@login_required
def avatar_detail(request):
    """ Displays the user's Punk and Stats """
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

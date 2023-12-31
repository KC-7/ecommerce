from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import AboutPage
from .forms import AboutPageForm


def about(request):
    """ Display list of about pages """
    about_pages = AboutPage.objects.all().order_by('-created_at')
    template = 'about/about.html'
    context = {'about_pages': about_pages}
    return render(request, template, context)


@login_required
def create_about_page(request):
    """ Create an about page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AboutPageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You created a new About Page')
            return redirect('about')

    form = AboutPageForm()
    template = 'about/create_about_page.html'
    context = {'form': form}
    return render(request, template, context)


def about_page_detail(request, pk):
    """ Display an about page """
    about_page = get_object_or_404(AboutPage, pk=pk)

    if request.method == 'POST':
        form = AboutPageForm(request.POST, instance=about_page)
        if form.is_valid():
            form.save()
            return redirect('about')

    form = AboutPageForm(instance=about_page)
    template = 'about/about_page_detail.html'
    context = {'about_page': about_page, 'form': form}
    return render(request, template, context)


@login_required
def delete_about_page(request, pk):
    """ Delete an about page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('about'))

    about_page = get_object_or_404(AboutPage, pk=pk)

    if request.method == "POST":
        username = request.POST.get("username")

        if username == request.user.username:
            about_page.delete()
            messages.success(request, 'About post deleted!')
            return redirect(reverse('about'))

        else:
            messages.error(
                request, 'Incorrect username. About page was not deleted.')

    template = 'about/about_page_detail.html'
    context = {
        'about_page': about_page,
    }

    return render(request, template, context)


@login_required
def edit_about_page(request, pk):
    """ Edit an about page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('about'))

    about = get_object_or_404(AboutPage, pk=pk)

    if request.method == 'POST':
        form = AboutPageForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated about page!')
            return redirect(reverse('about_page_detail', kwargs={'pk': pk}))
        else:
            messages.error(
                request,
                'Failed to update about page. Please ensure the form is valid.'
                )
    else:
        form = AboutPageForm(instance=about)
        messages.info(request, f'You are editing {about.title}')

    template = 'about/edit_about_page.html'
    context = {
        'form': form,
        'about': about,
    }

    return render(request, template, context)

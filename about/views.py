from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import AboutPage
from .forms import AboutPageForm


def about(request):
    about_pages = AboutPage.objects.all().order_by('-created_at')
    template = 'about/about.html'
    context = {'about_pages': about_pages}
    return render(request, template, context)


@login_required
def create_about_page(request):
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
    """ Delete an About Page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('about'))

    blog = get_object_or_404(AboutPage, pk=pk)
    blog.delete()
    messages.success(request, 'About Post Deleted!')
    return redirect(reverse('about'))

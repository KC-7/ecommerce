from django.shortcuts import render, redirect, get_object_or_404
from .models import AboutPage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    about_page = get_object_or_404(AboutPage, pk=pk)

    # Check if the user is a superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can delete about pages.')
        return redirect('about')

    if request.method == 'POST':
        about_page.delete()
        return redirect('about')

    template = 'about/delete_about_page.html'
    context = {'about_page': about_page}
    return render(request, template, context)

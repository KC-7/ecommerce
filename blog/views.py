from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import BlogPage
from .forms import BlogPageForm
from datetime import datetime


def blog(request):
    """ Display list of blog posts """
    blog_pages = BlogPage.objects.all().order_by('-created_at')
    template = 'blog/blog.html'
    paginate_by = 3  # paginate by posts (sets posts per page)
    paginator = Paginator(blog_pages, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'blog_pages': blog_pages,
        'is_paginated': page_obj.has_other_pages(),  # Sets 'is_paginated'
        }

    return render(request, template, context)


@login_required
def create_blog_page(request):
    """ Create a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You created a new Blog Page')
            return redirect('blog')
        else:
            messages.error(request, 'Form not valid.')

    form = BlogPageForm()
    template = 'blog/create_blog_page.html'
    context = {'form': form}
    return render(request, template, context)


def blog_page_detail(request, pk):
    """ Display a blog post """
    blog_page = get_object_or_404(BlogPage, pk=pk)

    # Get all blog pages ordered by created_at
    all_blog_pages = BlogPage.objects.all().order_by('created_at')

    # Find the index of the current blog page
    current_index = list(all_blog_pages).index(blog_page)

    # Calculate the index of the next and previous blog pages
    next_index = current_index + 1
    prev_index = current_index - 1

    next_blog_page = all_blog_pages[next_index] if next_index < len(all_blog_pages) else None
    prev_blog_page = all_blog_pages[prev_index] if prev_index >= 0 else None

    if request.method == 'POST':
        form = BlogPageForm(request.POST, instance=blog_page)
        if form.is_valid():
            form.save()
            return redirect('blog')

    form = BlogPageForm(instance=blog_page)
    template = 'blog/blog_page_detail.html'
    context = {
        'blog_page': blog_page,
        'form': form,
        'next_blog_page': next_blog_page,
        'prev_blog_page': prev_blog_page,
    }
    return render(request, template, context)


@login_required
def delete_blog_page(request, pk):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog_page = get_object_or_404(BlogPage, pk=pk)

    if request.method == "POST":
        username = request.POST.get("username")

        if username == request.user.username:
            blog_page.delete()
            messages.success(request, 'Blog post deleted!')
            return redirect(reverse('blog'))

        else:
            messages.error(
                request, 'Incorrect username. Blog post was not deleted.')
            return render(
                request, 'blog/delete_blog_page.html', {'blog_page': blog_page})

    template = 'blog/delete_blog_page.html'
    context = {
        'blog_page': blog_page,
    }

    return render(request, template, context)


@login_required
def edit_blog_page(request, pk):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('blog'))

    blog = get_object_or_404(BlogPage, pk=pk)

    if request.method == 'POST':
        form = BlogPageForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog_page_detail', kwargs={'pk': pk}))
        else:
            messages.error(
                request,
                'Failed to update blog page. Please ensure the form is valid.'
                )
    else:
        form = BlogPageForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog_page.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)

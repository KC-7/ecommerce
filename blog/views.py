from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import BlogPage
from .forms import BlogPageForm


def blog(request):
    blog_pages = BlogPage.objects.all().order_by('-created_at')
    template = 'blog/blog.html'
    paginate_by = 2  # paginate by posts (sets posts per page)
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You created a new Blog Page')
            return redirect('blog')

    form = BlogPageForm()
    template = 'blog/create_blog_page.html'
    context = {'form': form}
    return render(request, template, context)


def blog_page_detail(request, pk):
    blog_page = get_object_or_404(BlogPage, pk=pk)

    if request.method == 'POST':
        form = BlogPageForm(request.POST, instance=blog_page)
        if form.is_valid():
            form.save()
            return redirect('blog')

    form = BlogPageForm(instance=blog_page)
    template = 'blog/blog_page_detail.html'
    context = {'blog_page': blog_page, 'form': form}
    return render(request, template, context)


@login_required
def delete_blog_page(request, pk):
    """ Delete a Blog Post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('blog'))

    blog = get_object_or_404(BlogPage, pk=pk)
    blog.delete()
    messages.success(request, 'Blog Post Deleted!')
    return redirect(reverse('blog'))

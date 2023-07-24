from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogPageForm


def blog(request):
    blog_pages = BlogPage.objects.all().order_by('-created_at')
    template = 'blog/blog.html'
    context = {'blog_pages': blog_pages}
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
    blog_page = get_object_or_404(BlogPage, pk=pk)

    # Check if the user is a superuser
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only superusers can delete blog posts.')
        return redirect('blog')

    if request.method == 'POST':
        blog_page.delete()
        messages.success(request, 'You deleted the Blog Post')
        return redirect('blog')

    template = 'blog/delete_blog_page.html'
    context = {'blog_page': blog_page}
    return render(request, template, context)

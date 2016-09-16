from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone

from .models import Post
from .forms import PostForm


# blog
@login_required
def blog_admin(request):
    posts = Post.objects.all().order_by('-created_date')
    template_name = "blog/blog_admin.html"
    data = {'posts': posts}
    return render(request, template_name, data)

def blog_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        '-published_date')
    template_name = "blog/blog_posts.html"
    data = {'posts': posts}
    return render(request, template_name, data)

def blog_post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_post_detail.html', {'post': post})

# CRUD
@login_required
def create_post(request):
    if request.method == 'POST' and 'save' in request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:blog_admin')
    elif request.method == 'POST' and 'publish' in request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:blog_admin')
    else:
        form = PostForm()
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:blog_admin')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/blog_form.html',  {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if 'not-sure' in request.POST:
            return redirect('blog:blog_admin')
        post.delete()
        return redirect('blog:blog_admin')
    return render(request, 'blog/blog_confirm_delete.html', {'object': post})

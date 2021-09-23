from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm
# Create your views here.


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


# Add blog
@login_required
def add_blog_post(request):
    """
    Allow an admin user to add a blog post
    """
    if request.user.is_superuser:

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.info(request, 'Blog added successfully!')
                return redirect(reverse('article-detail', args=[post.id]))
            else:
                messages.error(request, 'Please check the form for errors. \
                        Blog failed to add.')
        else:
            form = PostForm()
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    template = 'add_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)

# Edit Blog Post
@login_required
def edit_blog(request, post_id):
    """
    Allow an admin user to edit a product to the store
    """
    if request.user.is_superuser:

        post = get_object_or_404(Post, pk=post_id)

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.info(request, 'Blog post updated successfully!')
                return redirect(reverse('article-detail', args=[post.id]))
            else:
                messages.error(request, 'Please check the form for errors. \
                    Blog post failed to update.')
        else:
            form = PostForm(instance=post)
            messages.info(request, f'Editing {post.title}')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    template = 'edit_blog.html'

    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


# Delete Blog Post
@login_required
def delete_blog(request, post_id):
    """
    Allow an admin user to delete a blog post
    """
    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        messages.info(request, 'Blog post deleted!')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    return redirect(reverse('blog'))

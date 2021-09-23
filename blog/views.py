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
                return redirect(reverse('blog', args=[post.id]))
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

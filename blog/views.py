from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import PostForm, CommentForm


# BlogView class using the post model
class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


# Blog article detail view
def detail(request, post_id):
    """
    This view displays individual blog posts & comments
    & allows admin and authenticated users to leave comments.
    The Blog itself and the comments are time & date stamped.
    """
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect(reverse('article-detail', args=[post.id]))
        else:
            messages.error(request, 'Please check the form for errors. \
                Comment failed to post.')
    else:
        comment_form = CommentForm()

    template = 'article_details.html'

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment,
    }

    return render(request, template, context)


# Add a blog post
@login_required
def add_blog_post(request):
    """
    This view will allow an admin user to add a blog post.
    This view also prevents non super users from adding posts.
    The "login_required" decorator, coupled with the superuser
    "IF" statemet check, prevents copy & paste of the url.
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


# Edit a Blog Post
@login_required
def edit_blog(request, post_id):
    """
    This view will allow an admin user to edit a blog post.
    This view also prevents non super users from editing posts.
    The "login_required" decorator, coupled with the superuser
    "IF" statemet check, prevents copy & paste of the url.
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


# Delete a Blog Post
@login_required
def delete_blog(request, post_id):
    """
    Allows an admin user to delete a blog post and redirect
    to the home page.
    """
    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        messages.info(request, 'Blog post deleted!')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    return redirect(reverse('blog'))


# Delete a Comment
@login_required
def delete_comment(request, comment_id):
    """
    Allows an admin user to delete a comment and redirect
    to the home page.
    """
    if request.user.is_superuser:
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
        messages.info(request, 'Comment deleted!')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    return redirect('blog')

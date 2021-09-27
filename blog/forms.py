from django import forms
from products.widgets import CustomClearableFileInput
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Creating the admin blog post form
    """
    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    """
    Creating the admin/user comment form
    """

    class Meta:
        model = Comment

        fields = (
            'comments',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comments'].widget.attrs[
            'placeholder'] = 'Enter your comment here..'
        self.fields['comments'].label = 'Leave a Comment'

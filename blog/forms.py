from django import forms
from products.widgets import CustomClearableFileInput
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


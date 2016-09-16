from django import forms

from .models import Post


# post form class
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input-title col-sm-12',
                'placeholder': 'Title...',
            }),
            'text': forms.Textarea(attrs={
                'class': 'input-text col-sm-12',
                'placeholder': 'Type the text here...',
            }),
        }

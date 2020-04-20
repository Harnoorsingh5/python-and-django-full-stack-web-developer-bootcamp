from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
        # widgets is way to connect classes with form fields
        widgets = {
            'author': forms.Select(attrs={'class': 'formfields'}),
            'title': forms.TextInput(attrs={'class': 'textinputclass formfields'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent formfields'}) 
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}) 
        }
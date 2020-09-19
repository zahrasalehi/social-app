from django.forms import ModelForm
from .models import Post

class CostumPostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'published_date']
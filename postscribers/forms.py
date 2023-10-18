from django import forms
from .models import PostModel

class PostModelForm(forms.ModelForm):
    # context = forms.CharField(widget=forms.Textarea(attrs={'rows':7}))
    class Meta:
        model = PostModel
        fields = ('title', 'context','date_created')
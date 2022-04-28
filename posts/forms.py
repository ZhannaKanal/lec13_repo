from tkinter import Widget
from django import forms
from .models import *

# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label="Esimi", widget=forms.TextInput(attrs={'class':'form-input'}))
#     slug = forms.SlugField(max_length=255,label="URL")
#     is_published = forms.BooleanField(label="Kelisim",required=False, initial=True)

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Poster
        fields="__all__"
        # fields=['','']
        widgets={
            'esim':forms.TextInput(attrs={'class':'form-input'}),
            'slug':forms.Textarea(attrs={'cols':50,  'rows':1}),
            'teg':forms.Textarea(attrs={'cols':50,  'rows':1})
        }
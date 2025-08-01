from django import forms 
from .models import Movie, Entry

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widget = {'text': forms.Textarea(attrs={'cols': 80})}
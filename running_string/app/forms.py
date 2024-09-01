from django import forms

class VideoForm(forms.Form):
    text = forms.CharField(label='Введите текст на англ', max_length=100, widget=forms.Textarea)

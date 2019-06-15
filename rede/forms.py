from django import forms

class PublicacaoForm(forms.Form):
    texto = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}))

class ComentarioForm(forms.Form):
    comentario = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'cols': 70, 'rows': 5}))
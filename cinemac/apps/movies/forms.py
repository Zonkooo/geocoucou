from django import forms

class ProfilForm(forms.Form):
    favouriteFilm = forms.CharField(max_length=100)


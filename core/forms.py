from django import forms
from .models import Annonce
from .models import Profil
class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titre', 'description', 'categorie', 'prix','image']
class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['telephone', 'photo']
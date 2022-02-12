from django.forms import ModelForm
from .models import Film, DodatkoweInfo, Ocena

class FilmForm(ModelForm):
      class Meta:
          model = Film
          fields = ['tittle', 'description', 'premiere', 'year', 'imdb_rating', 'img']

class DodatkoweInfoForm(ModelForm):
      class Meta:
          model = DodatkoweInfo
          fields = ['czas_trwania','gatunek']

class OcenaForm(ModelForm):
      class Meta:
          model = Ocena
          fields = ['gwiazdki', 'recenzja']
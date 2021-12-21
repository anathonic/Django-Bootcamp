from django.forms import ModelForm
from .models import Film

class FilmForm(ModelForm):
      class Meta:
          model = Film
          fields = ['tittle', 'description', 'premiere', 'year', 'imdb_rating', 'img']
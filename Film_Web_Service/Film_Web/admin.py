from django.contrib import admin
from .models import Film
# Register your models here.
#admin.site.register(Film)
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    fields = ["tittle", "description", "year", "img"]
    #exclude = ["description"]
    list_display = ["tittle", "year", "imdb_rating"]
    list_filter = ("year",)
    search_fields = ("tittle","year",)

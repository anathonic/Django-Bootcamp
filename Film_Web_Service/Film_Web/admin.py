from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Actor
# Register your models here.
#admin.site.register(Film)
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    fields = ["tittle", "description", "year", "img", "dodatkowe"]
    #exclude = ["description"]
    list_display = ["tittle", "year", "imdb_rating"]
    list_filter = ("year",)
    search_fields = ("tittle","year",)
admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Actor)
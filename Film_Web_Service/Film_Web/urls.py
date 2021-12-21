from django.urls import path
from Film_Web.views import filmy, nowy_film, edit, delete

urlpatterns = [
    path('all/', filmy, name="filmy"),
    path('new/', nowy_film, name="nowy_film"),
    path('update/<int:id>/', edit, name="edit"),
    path('delete/<int:id>', delete, name="delete"),
]

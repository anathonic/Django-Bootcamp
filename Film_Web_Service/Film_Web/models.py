from django.db import models

class DodatkoweInfo(models.Model):
     GATUNEK = {
          (0, 'Inne'),
          (1, 'Horror'),
          (2, 'Komedia'),
          (3, 'Sci-fi'),
          (4, 'Dramat'),


     }
     czas_trwania = models.PositiveSmallIntegerField(default=0)
     gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)
# Create your models here.
class Film(models.Model):
     tittle = models.CharField(max_length=64, blank=False, unique=True)
     year = models.PositiveSmallIntegerField(default=2000)
     description = models.TextField(default="")
     premiere  = models.DateField(null=True, blank=True)
     imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
     img = models.ImageField(upload_to="img", null=True, blank=True)
     dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE,  null=True, blank=True)
     def __str__(self):
          return self.tittle + ' (' + str(self.year) + ')'

     def tittle_with_year(self):
          return "{} ({})".format(self.tittle, self.rok)

class Ocena(models.Model):
     recenzja = models.TextField(default="", blank="True")
     gwiazdki = models.PositiveSmallIntegerField(default=5)
     film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Actor(models.Model):
     name = models.CharField(max_length=32)
     surname = models.CharField(max_length=32)
     filmy = models.ManyToManyField(Film)

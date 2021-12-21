from django.db import models

# Create your models here.
class Film(models.Model):
     tittle = models.CharField(max_length=64, blank=False, unique=True)
     year = models.PositiveSmallIntegerField(default=2000)
     description = models.TextField(default="")
     premiere  = models.DateField(null=True, blank=True)
     imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
     img = models.ImageField(upload_to="img", null=True, blank=True)

     def __str__(self):
          return self.tittle + ' (' + str(self.year) + ')'

     def tittle_with_year(self):
          return "{} ({})".format(self.tittle, self.rok)

     
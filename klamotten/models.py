from django.db import models

# Create your models here.
class Size(models.Model):
    size = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.size}"

class Artikel(models.Model):
    Name = models.CharField(max_length=64)
    size = models.ManyToManyField(Size)
    Artikelnummer = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.Name} {self.Artikelnummer}"

class ArtikelChosen(models.Model):
    Name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    Artikelnummer = models.IntegerField()

    def __str__(self):
        return f"{self.Name} Size:{self.size}"
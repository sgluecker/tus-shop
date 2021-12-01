from django.contrib import admin
from .models import Size, Artikel, ArtikelChosen

# Register your models here.
admin.site.register(Artikel)
admin.site.register(Size)
admin.site.register(ArtikelChosen)
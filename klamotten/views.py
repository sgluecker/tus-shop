from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Artikel, ArtikelChosen
from .forms import SizeForm


# Create your views here.

def index(request):
    return render(request, "klamotten/index.html", {
        "articles": Artikel.objects.all(),
        "articles_chosen":ArtikelChosen.objects.all()
    })

def auswahl(request, artikel_nummer):
    article = Artikel.objects.get(pk=artikel_nummer)
    return render(request, "klamotten/auswahl.html", {
        "article": article,
        "sizes": article.size.all()
    })

def add(request, artikel_nummer):
    size = request.POST["sizes"]
    article_ToAdd= Artikel.objects.get(pk=artikel_nummer)
    article_chosen_new = ArtikelChosen(Name=article_ToAdd.Name, size = size, Artikelnummer = article_ToAdd.Artikelnummer )
    article_chosen_new.save()
    return HttpResponseRedirect('/klamotten/')

def clearbasket(request):
    ArtikelChosen.objects.all().delete()
    return HttpResponseRedirect('/klamotten/')
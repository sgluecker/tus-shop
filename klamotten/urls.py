from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:artikel_nummer>", views.auswahl, name="Auswahl"),
    path("<int:artikel_nummer>/add", views.add, name="add"),
    path("clearbasket", views.clearbasket, name="clearbasket")
]
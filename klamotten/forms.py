from django import forms
from .models import Artikel

class SizeForm(forms.Form):
    size: forms.ModelMultipleChoiceField(queryset=Artikel.objects.all())
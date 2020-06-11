from django import forms
from .models import UPCard, Card


class CardForm(forms.ModelForm):
    class Meta:
        model = UPCard
        fields = '__all__'


class CreateCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

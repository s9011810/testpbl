from django import forms
from .models import UPCard, Card


class CardForm(forms.ModelForm):
    class Meta:
        model = UPCard
        fields = '__all__'


class CreateCardForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    context = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ))
    author = forms.IntegerField(
        widget=forms.Select()
    )

    class Meta:
        model = Card

        fields = '__all__'

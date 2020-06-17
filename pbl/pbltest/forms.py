from django import forms
from .models import UPCard, Card, User
from django.utils import timezone


class CardForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-controll form-control',
            'id': 'card_name',
            'name': 'card_name',
        }
    ))
    author = forms.ModelChoiceField(
        queryset=User.objects.filter(),
        widget=forms.Select(
            attrs={
                'class': 'form-controll form-control',
                'id': 'card-author',

            }
        )
    )
    cover = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control-file form-control-lg',
                'id': 'file',
                'name': 'file',

            }
        )
    )
    pdf = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control-file form-control-lg',
                'id': 'pdf',
                'name': 'pdf',

            }
        )
    )
    class_material = forms.ModelChoiceField(
        queryset=UPCard.objects.filter(class_material='test'),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'class_material',
            })
    )

    class Meta:
        model = UPCard
        fields = '__all__'


class CreateCardForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'card-title',
        }
    ))

    context = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'card-context',
        }
    ))

    author = forms.ModelChoiceField(
        queryset=User.objects.filter(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'card-author',

            }
        )
    )

    cover = forms.ModelChoiceField(
        queryset=UPCard.objects.filter(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'card-cover',
            })
    )

    class Meta:
        model = Card

        fields = '__all__'

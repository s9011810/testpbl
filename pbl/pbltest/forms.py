from django import forms
from login.models import CreateActivate, CreateClass
from .models import UPCard, Card, User, RowCard
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
    class_material = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'class_material',
        }
    ))
    activate_id = forms.ModelChoiceField(
        queryset=CreateActivate.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-controll form-control',
                'id': 'activate_id',

            }
        )
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
    context1 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'card-context1',
        }
    ))
    cover = forms.ModelChoiceField(

        queryset=UPCard.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'card-cover',
            }
        )
    )
    author = forms.ModelChoiceField(

        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'card-author',
            }
        )
    )

    class Meta:
        model = Card

        fields = '__all__'


class RowCreateCardForm(forms.ModelForm):
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
    context1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'card-context',
        }
    ))
    context2 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'card-context',
        }
    ))
    cover = forms.ModelChoiceField(

        queryset=UPCard.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'card-cover',
            }
        )
    )
    author = forms.ModelChoiceField(

        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'card-author',
            }
        )
    )

    class Meta:
        model = RowCard
        fields = '__all__'


class TestForm(forms.Form):
    image_data = forms.CharField(widget=forms.HiddenInput(), required=False)


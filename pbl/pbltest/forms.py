from django import forms
from .models import UPCard, Card, User
from django.utils import timezone
from crispy_forms.helper import FormHelper


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
        queryset=UPCard.objects.all(),
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


    class Meta:
        model = Card

        fields = '__all__'


class TestForm(forms.Form):
    image_data = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "agreement_form"
        self.helper.form_method = 'post'

        super(TestForm, self).__init__(*args, **kwargs)

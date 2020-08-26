from django import forms
from login.models import CreateActivate, CreateClass, Group, User
from .models import UPCard, Card, RowCard
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
                'class': 'form-control',
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
    class_material = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'class_material',
        }
    ))
    activate = forms.ModelChoiceField(
        queryset=CreateActivate.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-controll form-control',
                'id': 'activate',

            }
        )
    )
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'group',

            }
        )
    )

    class Meta:
        model = UPCard
        fields = ('title','author','cover','class_material','activate','group')


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
    activate = forms.ModelChoiceField(
        queryset=CreateActivate.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-controll form-control',
                'id': 'activate',

            }
        )
    )
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'group',

            }
        )
    )

    class Meta:
        model = Card
        fields = ('title', 'context', 'author', 'context1', 'cover', 'activate', 'group')


class RowCreateCardForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'card-title',
        }
    ))

    context = forms.CharField(widget=forms.TextInput(
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
    activate = forms.ModelChoiceField(
        queryset=CreateActivate.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'activate',

            }
        )
    )
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'group',

            }
        )
    )

    # activte = forms.ModelChoiceField(
    #
    #     queryset=CreateActivate.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'card-activate',
    #         }
    #     )
    # )
    # group = forms.ModelChoiceField(
    #
    #     queryset=Group.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'card-group',
    #         }
    #     )
    # )

    class Meta:
        model = RowCard
        fields = ('title', 'context', 'context1', 'context2', 'cover', 'activate','group')


class TestForm(forms.Form):
    image_data = forms.CharField(widget=forms.HiddenInput(), required=False)


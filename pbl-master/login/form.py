from django import forms
from .models import Group, CreateActivate, CreateClass


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))


class RegisterForm(forms.Form):
    c_name = forms.CharField(label="中文名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = (
        ('guest', "訪客"),
        ('teacher', "引導師"),
    )
    username = forms.CharField(label="用戶名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="確認密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    identify = forms.ChoiceField(label='身分', choices=gender, widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'login-identyfy',
            }
        ))


class GroupForm(forms.Form):
    groupname = forms.CharField(label="群組名稱", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ClassForm(forms.ModelForm):
    class_title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'class_title',
        }
    ))

    class Meta:
        model = CreateClass

        fields = '__all__'


class ActivateForm(forms.ModelForm):
    activate_name = forms.CharField(label="活動名稱", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CreateActivate
        fields = '__all__'


class CreateGroup(forms.ModelForm):
    group = forms.CharField(label="群組名稱", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    activate = forms.ModelChoiceField(
        queryset=CreateActivate.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'group-activate',
            }
        )
    )

    class Meta:
        model = Group
        fields = ('group', 'activate', 'group_user')

from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-nickname",
        "placeholder": "Введите ваш никнейм",
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-password",
        "placeholder": "Введите ваш пароль",
        }))
    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-nickname",
        "placeholder": "Введите ваш никнейм",
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-email",
        "placeholder": "Введите вашу почту",
    }))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        "class": "form-phone_number",
        "placeholder": "Введите номер телефона",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-password1",
        "placeholder": "Придумайте пароль",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-password2",
        "placeholder": "Введите пароль еще раз",
    }))
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "password1", "password2")


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-username", 
        "readonly": True
        }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-first_name"
        }), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-last_name"
        }), required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-email", 
        "readonly": True
        }))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        "class": "form-phone_number"
        }), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "form-user_photo", 
        "onchange": "previewImage(event)"
        }), required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "phone_number", "image")

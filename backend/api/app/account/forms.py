from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class AuthenticationUserForm(AuthenticationForm):
    pass


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"autocomplete": "email", "class": "reg-menu__input"}
        )
    )
    def clean_username(self):
        data = self.cleaned_data["username"]
        if User.objects.filter(username=data).exists():
            raise ValidationError(_("Пользователь с таким именем уже существует"))
        return data

    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise ValidationError(_("Пользователь с такой почтой уже существует"))
        return data

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True

        if commit:
            user.save()
        return user
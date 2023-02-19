from django import forms
from django.core.validators import MinLengthValidator
from django.contrib.auth import authenticate
from .models import User

class SinginForm(forms.Form):
    username = forms.CharField(label='Nome de usuario:', max_length=100, widget=forms.TextInput(attrs={'class': 'login-input'}))
    email = forms.EmailField(label='Email:', max_length=100, widget=forms.TextInput(attrs={'class': 'login-input'}))
    password = forms.CharField(label='Senha:', max_length=100, widget=forms.PasswordInput(attrs={'class': 'login-input'}), min_length=8)
    confirm_password = forms.CharField(label='Confirme a sua senha:', max_length=100, widget=forms.PasswordInput(attrs={'class': 'login-input'}), min_length=8)
    endereco = forms.CharField(label='Endereço:', max_length=100, widget=forms.TextInput(attrs={'class': 'login-input', 'placeholder': 'Rua... Bairo... Numero...'}))
    telefone = forms.CharField(label='Telefone(Com DDD):', max_length=11, validators=[
        MinLengthValidator(11)
    ], widget=forms.TextInput(attrs={'class': 'login-input', 'placeholder': '86988887777'}))
    first_name = forms.CharField(label='Nome:', max_length=100, widget=forms.TextInput(attrs={'class': 'login-input'}))
    last_name = forms.CharField(label='Sobrenome:', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'login-input'}))
    def clean(self):
        data = super(SinginForm, self).clean()
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        username = data.get("username")
        user_exists = User.objects.filter(username=username)
        if user_exists:
            raise forms.ValidationError(
                "Nome de usuario já exite"
            )

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuario:', max_length=100, widget=forms.TextInput(attrs={'class': 'login-input'}))
    password = forms.CharField(label='Senha:', max_length=100, widget=forms.PasswordInput(attrs={'class': 'login-input'}), min_length=8)
    def clean(self):
        data = super(LoginForm, self).clean()
        password = data.get("password")
        username = data.get("username")

        user_exists = authenticate(username=username, password=password)
        if user_exists:
            self.user = user_exists
        else:
            raise forms.ValidationError(
                "Nome de usuário ou Senha incorreto"
            )
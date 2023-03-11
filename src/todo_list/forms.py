from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'h-5 items-center pl-4',
                'placeholder': "Username",
                'id': 'username-field'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'h-5 items-center pl-4',
                'placeholder': "Password",
                'id': 'password-field'
            }
        )
    )

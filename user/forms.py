from django import forms
from .models import User
from random import choice
import string

def random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(8):
        password += choice(characters)
    return password

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'data_de_nascimento', 'senha']

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) == 0:
            senha = random_password()
            return senha
        else:
            return senha
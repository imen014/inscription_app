from django import forms
from account_creation_app.models import UserCreationModel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model


class UserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationModel
        fields = ['username', 'email', 'image', 'date_naissance','lieu_residence','social_media','description','current_employment','academic_degrees','professional_skills','hobbies']


class AuthenticatorForm(forms.Form):
    username=forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    
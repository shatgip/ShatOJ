from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField()
    gender = forms.CharField(max_length=10)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', 'gender')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

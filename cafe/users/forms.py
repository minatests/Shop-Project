from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["phone_number", "first_name","last_name", "password1", "password2"]


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["phone_number", "password"]

class StaffLoginForm(forms.Form):
    phone_number=forms.CharField(label="PHONE NUMBER",max_length=11)

class StaffOtpForm(forms.Form):
    code=forms.IntegerField()


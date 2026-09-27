from django import forms
from .models import Leadt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from .models import User
User = get_user_model()

class LeadForm(forms.ModelForm):
    class Meta:
        model = Leadt
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

from django import forms
from .models import Leadt

class LeadForm(forms.ModelForm):
    class Meta:
        model = Leadt
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )
    
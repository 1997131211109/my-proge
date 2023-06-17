from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'date_of_birth','first_name', 'last_name', 'email', 'gender']

from django import forms
from app_two.models import User

class NewUserForm(forms.ModelForm):
    # Inline class
    class Meta():
        model = User
        fields = '__all__'

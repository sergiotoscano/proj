from django import forms
from django.core import validators
from waitinglist.models import NewUserModel

class NewUserForm(forms.ModelForm):

    class Meta:
        model = NewUserModel
        fields = '__all__'
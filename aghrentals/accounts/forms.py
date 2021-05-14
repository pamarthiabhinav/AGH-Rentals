from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from django.forms.widgets import EmailInput

# Create your views here.


class CreateUserForm(UserCreationForm):
    firstName = forms.CharField(
        label="First Name", required=True, widget=forms.TextInput)
    lastName = forms.CharField(
        label="Last Name", required=True, widget=forms.TextInput)
    email = forms.EmailField(
        label="Email", required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email',
                  'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["firstName"]
        user.last_name = self.cleaned_data["lastName"]
        if commit:
            user.save()
        return user

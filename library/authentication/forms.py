from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Email:',
                               widget=forms.TextInput())
    password = forms.CharField(label='Password:',
                               widget=forms.PasswordInput())


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(label='E-mail', widget=forms.EmailInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
            'middle_name': 'Middle name'
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Email exists!!!')
        return email


class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'middle_name', 'role', 'is_active', 'is_staff', 'is_superuser']
        labels = {
            'email': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
            'middle_name': 'Middle name',
            'role': 'Role',
            'is_active': 'Active',
            'is_staff': 'Staff',
            'is_superuser': 'Super user',
        }


class ProfileUserForm(forms.ModelForm):
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.EmailInput())
    first_name = forms.CharField(disabled=True, label='First name', widget=forms.TextInput())
    last_name = forms.CharField(disabled=True, label='Last name', widget=forms.TextInput())
    middle_name = forms.CharField(disabled=True, label='Middle name', widget=forms.TextInput())

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'middle_name', 'email']


class EditProfileUserForm(forms.ModelForm):
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.EmailInput())

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'middle_name', 'email']
        labels = {
            'email': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
            'middle_name': 'Middle name'
        }

        
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput())

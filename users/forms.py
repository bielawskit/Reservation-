from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class RegistrationFormUser(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('name', 'surname', 'email', 'telephone_number', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()

        return user


class RegistrationFormClub(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('name', 'surname', 'email', 'NIP', 'telephone_number', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))
    password = forms.CharField(label='Hasło',widget=forms.PasswordInput(attrs={
        'placeholder': 'Hasło'
    }))

    class Meta:
        fields = ('username', 'password')

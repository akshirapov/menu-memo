from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        dupls = User.objects.exclude(pk=self.instance.pk).filter(email=email)
        if dupls.exists():
            raise forms.ValidationError(
                _('A user with that email already exists.'),
                code='email_exist',
            )
        return email

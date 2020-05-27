from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(forms.ModelForm):
    """
    A form containing form fields for register a new user.
    """
    email = forms.EmailField(
        label=_('Email')
    )
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("Make sure it's at least 8 characters including a number and a lowercase letter."),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = True
        self.fields['username'].help_text = ''

    def clean_email(self):
        email = self.cleaned_data['email']
        # check for the same email
        user = User.objects.filter(email=email).first()
        if user is not None:
            raise forms.ValidationError(
                _("A user with that email already exists.")
            )
        return email

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

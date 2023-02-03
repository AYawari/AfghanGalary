from django import forms
from . import models
from django.contrib.auth.models import User


class signup_form(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    confirm_p = forms.CharField(label="confirm", widget=forms.PasswordInput)

    class Meta:
        model = User
        help_texts = {"username": None}
        fields = ("username", "first_name", "email")

    def clean_confirm(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("confirm_p"):
            return self.cleaned_data.get("confirm_p")
        else:
            raise forms.ValidationError("not match it you password")

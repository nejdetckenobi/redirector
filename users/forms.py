from django.contrib.auth.forms import (UserCreationForm as BaseUserCreationForm,  # NOQA
                                       UserChangeForm as BaseUserChangeForm)
from django import forms
from .models import User


class UserCreationForm(BaseUserCreationForm):

    class Meta(BaseUserCreationForm):
        model = User
        fields = ('username', 'email')


class UserChangeForm(BaseUserChangeForm):

    class Meta(BaseUserChangeForm):
        model = User
        fields = ('username', 'email')

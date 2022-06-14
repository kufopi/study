from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']


class RoomForm(ModelForm):
    """Form definition for Room."""

    class Meta:
        """Meta definition for Roomform."""

        model = Room
        fields = '__all__'
        exclude = ['participants', 'host']


class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ('name',"username",'email', 'avatar','bio')


from django import forms
from django.forms import ModelForm
from main_f.models import Message, User_list


class UserForm(ModelForm):
    class Meta:
        model = User_list
        fields = ['login', 'password']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'text_input',
                'required': True,
                'value': '',
            }),
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['reciever', 'text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'text_input',
                'required': True,
                'value': '',
            }),
        }

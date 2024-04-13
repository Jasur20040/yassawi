from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractUser
from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class KyrsForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].empty_label = "-----"

    class Meta:
        model = Kyrs
        fields = (
        "name", "img", "category", "money", "content", "lan","url")
        widgets = {
            'content': forms.Textarea(attrs={'cols': 10, 'rows': 10}),
        }



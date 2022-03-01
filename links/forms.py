from django import forms
from .models import Link


class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url', )
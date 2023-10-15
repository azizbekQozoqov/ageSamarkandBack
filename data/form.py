from django import forms
from .models import Building


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['id','year','address','floors','type','images','poly']

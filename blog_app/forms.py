from django import forms
from .models import blog_model

class blog_form(forms.ModelForm):
    class Meta:
        model = blog_model
        fields='__all__'


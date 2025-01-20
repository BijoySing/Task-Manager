from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoryName']
        widgets = {
            'categoryName': forms.TextInput(attrs={'class': 'form-control'}),
        }

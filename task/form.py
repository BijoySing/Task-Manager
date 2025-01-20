from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'categories', 'is_completed']
        widgets = {
            'taskTitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'taskDescription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description', 'rows': 4}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control '}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'accent-color: green;'}),
        }

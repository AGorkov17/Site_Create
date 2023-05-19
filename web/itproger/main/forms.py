from .models import Articles
from django.forms import ModelForm, TextInput, FloatField

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'vol', 'non']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Никнэйм'
            }),
            "vol": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите 0'
            }),
            "non": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите 0'
            }),
        }

class AutoForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Никнэйм'
            }),
        }
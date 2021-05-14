from .models import Place, Profile
from django.forms import ModelForm, TextInput, Textarea


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ["name", "comment","latitude", "longitude"]
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название места'}),
            "comment": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваши впечатления'}),
            "latitude": TextInput(attrs={'class': 'form-control', 'placeholder': 'Широта'}),
            "longitude": TextInput(attrs={'class': 'form-control', 'placeholder': 'Долгота'}),
        }


from django.forms import ModelForm
from .models import Dog
from django.forms.models import inlineformset_factory

class DogForm(ModelForm):
    class Meta:
        model = Dog
        exclude = ['like']

class UpdateForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['photo', 'age', 'location', 'favourite_food']
from django import forms
from django.forms import ModelForm
from .models import CrowdData

class DataForm(ModelForm):
    CROWD_LEVEL_CHOICES = [(i, str(i)) for i in range(0, 11)]

    crowd_level = forms.ChoiceField(choices=CROWD_LEVEL_CHOICES, label="混雑状況もしくは並び時間")

    class Meta:
        model = CrowdData
        fields = ["location", "crowd_level"]

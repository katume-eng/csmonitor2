from django.forms import ModelForm
from .models import CrowdData

class DataForm(ModelForm):
    class Meta:
        model = CrowdData
        fields = ["location","crowd_level",]
    

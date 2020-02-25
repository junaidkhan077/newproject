from django import forms  
from Hero.models import Hero
class HeroForm(forms.ModelForm):  
    class Meta:  
        model = Hero  
        fields = "__all__"

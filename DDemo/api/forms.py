from django import forms
from .models import Person

class PersoneqwForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
    
    
class Pjnbhbd(forms.Form):
    fname = forms.CharField(max_length=20)
    lname = forms.CharField(max_length=20)
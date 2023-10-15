from django import forms
from .models import Apply , jobs

class ApplyForm (forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'webiste','cv','cover_letter']
        widgets = {
            'created_at': forms.DateTimeInput(attrs={'readonly': True}) 
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = jobs
        fields = '__all__'
        exclude = ['owner','slug', 'image']
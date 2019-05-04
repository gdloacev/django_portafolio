from django import forms
from data import models

"""class ProjectForm(forms.Form):
    title = forms.CharField(label='Name of Project', required=True, 
    widget=forms.TextInput)
    description = forms.CharField(label='Description', required=True, 
    widget=forms.Textarea)
    image = forms.ImageField(label='Picture', required=False, widget=forms.FileInput)
    link = forms.URLField(label='URL of Project', widget=forms.TextInput)"""

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('title', 'description', 'image', 'link')
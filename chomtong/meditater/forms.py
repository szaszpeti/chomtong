from django.forms import ModelForm
from django import forms
from .models import Meditater

class MeditaterForm(ModelForm):
    class Meta:
        model = Meditater
        fields = ['course_type',
                  'name',
                  'state',
                  'email',
                  'gender',
                  'born',
                  'profession']



class UploadFileForm(forms.Form):
    file = forms.FileField()
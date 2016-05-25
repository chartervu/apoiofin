from django.forms import ModelForm

from models import Detail, Organ

class DetailForm(ModelForm):
    class Meta:
        model = Detail
        exclude = ['club']

class OrganForm(ModelForm):
    class Meta:
        model = Organ
        exclude = ['club']

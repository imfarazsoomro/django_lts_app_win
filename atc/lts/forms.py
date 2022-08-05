from django import forms
from constants import SERVICE_STATUS_CHOICES


class AddNewRequestForm(forms.Form):
    ref = forms.IntegerField()
    title = forms.CharField()
    price = forms.IntegerField()
    due_date = forms.DateField()
    status = forms.ChoiceField(choices=SERVICE_STATUS_CHOICES, default='request')

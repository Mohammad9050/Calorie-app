from django import forms


class AddForm(forms.Form):
    name = forms.CharField(max_length=100,required=False ,widget=forms.TextInput())

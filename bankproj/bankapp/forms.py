from django import forms


class Form(forms.ModelForm):
    name = forms.CharField(max_length=250)

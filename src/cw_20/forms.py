from django import forms


class CreateCustomerForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    profession = forms.CharField(max_length=200)
    age = forms.IntegerField()
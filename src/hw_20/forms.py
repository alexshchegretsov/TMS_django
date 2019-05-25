from django import forms


class CarForm(forms.Form):
    brand = forms.CharField(max_length=30)
    model = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    weight = forms.IntegerField()
    owner_full_name = forms.CharField(max_length=50)
    year_issue = forms.IntegerField()

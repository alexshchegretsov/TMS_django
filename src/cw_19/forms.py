from django import forms

class WriteNewPost(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0, max_value=99)
    comment = forms.CharField(max_length=300)

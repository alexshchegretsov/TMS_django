from django import forms


class TicketHandler(forms.Form):
    full_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Alex Shchegretsov'}))
    from_where = forms.CharField(max_length=20,initial='Minsk')
    to_where = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'for example Moscow'}))
    how_many_people = forms.IntegerField(min_value=1)
    date = forms.DateField(widget=forms.SelectDateWidget)



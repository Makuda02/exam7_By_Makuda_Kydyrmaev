from django import forms


class Guest_booksForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label='Имя')
    email = forms.EmailField(max_length=60, required=True,  label='Почта')
    description = forms.CharField(max_length=60, required=True, label='Описание')

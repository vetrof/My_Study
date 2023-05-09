from django import forms


class HousesFilterForm(forms.Form):
    min_price = forms.IntegerField(label='от', required=False)
    max_price = forms.IntegerField(label='до', required=False)
    query = forms.CharField(label='Описание', required=False)
    ordering = forms.ChoiceField(label='Сортировка', required=False, choices=[
        ('name', 'по алфавиту'),
        ('price', 'сначала недорогие'),
        ('-price', 'сначала дорогие'),
    ])

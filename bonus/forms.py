from django import forms
from bonus.choices import *



class LoyaltyStatusForm(forms.Form):
    status_field = forms.ChoiceField(choices=CARD_STATUS)


class LoyaltyGeneratorForm(forms.Form):
    serial = forms.CharField(max_length=4)
    expiried_time = forms.ChoiceField(choices=EXPIRATION_TIME_CHOISES)
    number_of_generated_cards = forms.IntegerField()


class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    q = forms.DateField(widget=DateInput)

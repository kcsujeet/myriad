from django import forms
from django.forms import ModelForm, Select, TextInput
from events.models import *



class LoginForm(forms.Form):
  	username = forms.CharField(
  		widget=forms.TextInput(
  			attrs={'class': 'form-control'}))
  	password = forms.CharField(
  		widget=forms.PasswordInput(
  			attrs={'class': 'form-control'}))

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'description', 'date_time', 'venue', 'venue_url','signup_form_code']
        labels = {
            "event_name": "",
            "description": "",
            'date_time':"",
             "venue":"",
             "venue_url":"",
             "signup_form_code":""
        }

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['event_name'].widget.attrs['placeholder'] = 'Event Name'
       self.fields['description'].widget.attrs['placeholder'] = 'Description'
       self.fields['date_time'].widget.attrs['placeholder'] = 'Date Time'
       self.fields['venue'].widget.attrs['placeholder'] = 'Venue'
       self.fields['venue'].widget.attrs['id'] = 'autocomplete'
       self.fields['venue_url'].widget.attrs['placeholder'] = 'Venue URL'
       self.fields['signup_form_code'].widget.attrs['placeholder'] = 'Eloqua Signup Form Code'
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class': 'form-control'
           })
           
from django import forms
from django.utils.safestring import mark_safe

class NameForm(forms.Form):
	Subject = forms.CharField(label='Subject', max_length=100)
	Recipient_Email_Address = forms.CharField(label='Recipient\'s Email Address', max_length=100)
	Board_Id = forms.CharField(label='Trello Board Id', max_length=100)
	apikey = forms.CharField(label='Trello API Key', max_length=100)
	tocken = forms.CharField(label='Trello Tocken', max_length=100) 
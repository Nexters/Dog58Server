from django import forms

class boardForm(forms.Form) :
	title = forms.CharField(label='title', max_length=200)
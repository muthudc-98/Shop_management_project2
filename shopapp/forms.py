from django import forms

from django.contrib.auth.models import User

from shopapp.models import Shopview

class Signupform(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password','email','first_name','last_name']


class Shopform(forms.ModelForm):
	class Meta:
		model=Shopview
		fields='__all__'
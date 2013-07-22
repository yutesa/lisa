from django.forms import ModelForm
from django import forms
from yutesapp.models import UsersLikesUnlikes

class LikeForm(ModelForm):
	class Meta:
		model = UsersLikesUnlikes
from django import forms
from .models import UploadImage


class ContactForm(forms.Form):
	full_name = forms.CharField(max_length=50)
	email = forms.EmailField()
	message = forms.CharField(max_length=800, widget=forms.Textarea())

class UploadImageForm(forms.ModelForm):
	class Meta:
		model = UploadImage
		fields = ['image_name', 'location', 'image']
from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class contactForm(forms.Form):
	name = forms.Charfield(required=False, max_length=100, help_text="not more than 100 characters only")
	email = forms.EmailField(required=True)
	comment = forms.Charfield(required=True, widget=forms.Textarea)
	captcha = ReCaptchaField(widget=ReCaptchaWidget())
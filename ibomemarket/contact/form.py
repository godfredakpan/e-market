from django import forms

class contactForm(forms.Form):
	name = forms.CharField(required=False, max_length=100, help_text="Not more than 100 characters only")
	email = forms.EmailField(required=True)
	comment = forms.CharField(required=True, widget=forms.Textarea)

# class ReCaptchaWidget(Widget):
#     def __init__(self, explicit=False, container_id=None, theme=None, type=None, size=None, tabindex=None,
#                  callback=None, expired_callback=None, attrs={}, *args, **kwargs):
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

	title   	= forms.CharField(label = '',
					 widget = forms.TextInput(attrs = {"placeholder": "Your title"	}))
	email       = forms.EmailField()
	description = forms.CharField(
							required = False,
							widget = forms.Textarea(
									attrs = {
										"placeholder": "Your description",
										"id": "my-id-for-textarea",
										"class": "new-class-name two",
										"rows": 10,
										"cols": 50
									}
								)
							)
	price       = forms.DecimalField(initial = 129.99)
	class Meta:
		model = Product
		fields = [
		'title',
		'description',
		'price'
		]
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("This is not a valid title")
		if not "news" in title:
			raise forms.ValidationError("This is not a valid title")
		return title

	def clean_email(self, *args, **kwargs):
		title = self.cleaned_data.get("email")
		if not email.endwith("edu"):
			raise forms.ValidationError("This is not a valid email")
		return email


class RawProductForm(forms.Form):
	title   	= forms.CharField(label = '', widget = forms.TextInput(attrs = {"placeholder": "Your title"	}))
	description = forms.CharField(
							required = False,
							widget = forms.Textarea(
									attrs = {
										"placeholder": "Your description",
										"id": "my-id-for-textarea",
										"class": "new-class-name two",
										"rows": 20,
										"cols": 50
									}
								)
							)
	price       = forms.DecimalField(initial = 129.99)

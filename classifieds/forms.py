from django import forms
from classifieds.models import *


CHOICES = (
		(1,"Books"),
		(2,"Furniture"),
		(3,"Events & Tickets"),
		(4,"Jobs"),
		(5,"Tutors"),
		

		)
class AdForm(forms.ModelForm):

	try:
		cat = category_of_classifieds.objects.order_by('-name')
		
		
		category = cat

	except category_of_classifieds.DoesNotExist:
		category= forms.ChoiceField(choices=CHOICES)
	title  = forms.CharField(max_length=200, )
	description = forms.CharField(widget=forms.Textarea, initial = "Enter price and other relevant information here.")
	
	class Meta:
		# Provide an association between the ModelForm and a model
		model = model_for_individual_listing
		fields = ('category','title','description',)




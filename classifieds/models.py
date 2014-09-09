from django.db import models
from django.contrib import admin

class category_of_classifieds(models.Model):
	name = models.CharField(max_length = 20, unique =True)

	def __unicode__(self):
		return self.name

class ad(models.Model):
	# category = models.OneToOneField(category_of_classifieds) # pair the ad with the category it belongs to with a one to many relationship
	title = models.CharField(max_length=128,unique=True)
	
	
	# choice_for_ad = models.IntegerField(choices=CHOICES)
	description =  models.CharField(max_length=1000)

	def __unicode__(self):
		return self.title

class model_for_individual_listing(models.Model):

	LIKE_NEW = 1
	ACCEPTABLE =2 
	GOOD =3
	FAIR = 4
	POOR = 5

	CHOICES_FOR_CONDITION = (
			(LIKE_NEW,"Like new"),
			(ACCEPTABLE, "Acceptable"),
			(GOOD, "Good"),
			(FAIR, "Fair"),
			(POOR, "Poor")
		)
	
	category= models.ForeignKey(category_of_classifieds)
	title = models.CharField(max_length=1000,unique=False)

	description =  models.CharField(max_length=1000)
	cost = models.IntegerField()
	condition = models.CharField(max_length=10)
	docfile = models.CharField(max_length=10)


	def __unicode__(self):
		return self.title
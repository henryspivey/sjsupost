from django.contrib import admin
from classifieds.models import category_of_classifieds,ad,model_for_individual_listing

admin.site.register(category_of_classifieds) # register the models in the admin
admin.site.register(ad)
admin.site.register(model_for_individual_listing)
# admin.site.register(AdAdmin)


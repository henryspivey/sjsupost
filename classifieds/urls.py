from django.conf.urls import patterns, url
from classifieds import views
from django.conf import settings



from django.contrib import admin # needed to register the models in the admin interface
admin.autodiscover()
urlpatterns = patterns('',
        url(r'^$', views.index, name='context_dict'),  # link to views in app (classifieds)
        url(r'^about/', views.about,name ='about'),
        url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
        url(r'^category/(?P<category_name_url>.+?)/(?P<listing_name_url>.+?)/$', views.listingz, name='listingz'),
        url(r'^add_listing/', views.add_listing, name='add_listing'),

        

)




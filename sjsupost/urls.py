from django.conf.urls import patterns, include, url
from django.conf import settings  # gives me access to variables in settings
from django.contrib import admin
admin.autodiscover()

from .profiles.views import *

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', include('classifieds.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^classifieds/', include('classifieds.urls')), # links to the app
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include("account.urls")),

    url(r"^profile/edit/", ProfileEditView.as_view(), name="profiles_edit"),
    url(r"^u/$", ProfileListView.as_view(), name="profiles_list"),

    url(r"^u/(?P<username>[\w\._-]+)/$", ProfileDetailView.as_view(), name="profiles_detail"),
    url(r'^messages/', include("django_messages.urls"), name='messages'),

    


)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )    
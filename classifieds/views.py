from django.template import RequestContext
from django.shortcuts import render_to_response
from classifieds.models import *
from django.utils.encoding import iri_to_uri
from classifieds.forms import AdForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import urllib
import django
from django_messages.utils import format_quote, get_user_model, get_username_field

User = get_user_model()


def encode_url(url):
	return iri_to_uri(url)
def index(request):
	# Request the context of the request.
    # The context contains information such as the client's machine details, for example.
	context = RequestContext(request)


	# Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
	category_list = category_of_classifieds.objects.order_by('-name')

	ad_list = ad.objects.order_by('-id')
	
	listings_by_title = model_for_individual_listing.objects.all().order_by('-category')


	
	context_dict = {'categories': category_list, 'ads':ad_list, 'listings':listings_by_title,}

	


	# Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    # The render_to_response() function will take this data and mash it together 
    # with the template to produce a complete HTML page.
	return render_to_response("classifieds/index.html",context_dict,context)

def about(request):
	context = RequestContext(request)

	return render_to_response("classifieds/about.html",context)

def category(request,category_name_url):
	# request our context from the request passed to us
	context = RequestContext(request)

	# change underscores in the category name to spaces
	# makes it easier to work with
	category_name = urllib.unquote(category_name_url).decode('utf8')
	

	# start building a dictionary to pass the category name into the template
	context_dict = {'category_name':category_name}

	try:

		category = category_of_classifieds.objects.get(name=category_name)

		listings = model_for_individual_listing.objects.filter(category=category) # filter the ads per their category

		# add the ads and the category to what we'll pass in the template
		context_dict['listings'] = listings

		context_dict['category'] = category

	except category_of_classifieds.DoesNotExist:
		pass
	return render_to_response('classifieds/category.html',context_dict,context)

def get_user_model():
    if django.VERSION[:2] >= (1, 5):
        from django.contrib.auth import get_user_model
        return get_user_model()
    else:
        from django.contrib.auth.models import User
        return User


def get_username_field():
    if django.VERSION[:2] >= (1, 5):
        return get_user_model().USERNAME_FIELD
    else:
        return 'username'

def listingz(request,category_name_url,listing_name_url):

	context = RequestContext(request)

	listing_name =  urllib.unquote(listing_name_url).decode('utf8')

	
	listing_price = model_for_individual_listing.objects.order_by('-cost').filter(title__exact=listing_name).values('cost')[0].get('cost')


	category_name = urllib.unquote(category_name_url).decode('utf8')

	listing_cond = model_for_individual_listing.objects.order_by('-condition').filter(title__exact=listing_name).values('condition')[0].get('condition')
	
	listing_image = model_for_individual_listing.objects.order_by('-image').filter(title__exact=listing_name).values('image')[0].get('image')

	

	context_dict = {'listing_name':listing_name,'category_name':category_name,'listing_price':listing_price,'listing_cond':listing_cond,'listing_image':listing_image,}

	
	return render_to_response('classifieds/listing.html',context_dict,context)
	



def add_listing(request):

	context = RequestContext(request)

	# an HTTP Post?
	if request.method == 'POST':
		form = AdForm(request.POST,request.FILES)

		if form.is_valid():
			form.save(commit=True)

			return HttpResponseRedirect('/classifieds')

		else:
			print form.errors

	else:
		form = AdForm()

	return render_to_response('classifieds/add_listing.html',{'form':form},context)

def search(request):
	if request.metho=='GET':
		query = request.GET.get('q')
		return render_to_response(query,context)

	
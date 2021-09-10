from django.shortcuts import render, redirect
from event.models import Event




def home_view(request):

	events = Event.objects.all()


	context = {
		"events":events,

	}
	return render(request, 'base/index.html', context)



def about_view(request):

	context = {

	}
	return render(request, 'base/about.html', context)



def contact_view(request):

	context = {

	}
	return render(request, 'base/contact.html', context)

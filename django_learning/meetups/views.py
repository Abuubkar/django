from django.shortcuts import render
from django.http import HttpResponse

from .models import Meetup

# Create your views here.

def index(request):
    #no need to specify templates folder in PATH
    meetups = Meetup.objects.all()
    
    return render(request,'meetups/index.html',{
        'show_meetups':True,
        'meetups':meetups
    }) 
    # return HttpResponse('Hello World!');

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html',{
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_desccription': selected_meetup.description
            })
    except Exception as err:
        return render(request, "meetups/meetup-details.html",{'meetup_found': False},)

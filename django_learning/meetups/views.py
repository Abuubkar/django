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
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup', 
        'description': 'This is the first meetup!'
        }
    return render(request, 'meetups/meetup-details.html',{
        'meetup_title': selected_meetup['title'],
        'meetup_desccription': selected_meetup['description']
        })
    
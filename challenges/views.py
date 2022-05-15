from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Qui occaecat mollit reprehenderit adipisicing incididunt eiusmod mollit reprehenderit ex minim.",
    "may": "Qui occaecat mollit reprehenderit adipisicing incididunt eiusmod mollit reprehenderit ex minim.",
    "june": "Qui occaecat mollit reprehenderit adipisicing incididunt eiusmod mollit reprehenderit ex minim.",
    "july": "Qui occaecat mollit reprehenderit adipisicing incididunt eiusmod mollit reprehenderit ex minim.",
    "august": "Qui occaecat mollit reprehenderit adipisicing incididunt eiusmod mollit reprehenderit ex minim.",
    "september": "Qui occaecat mollit reprehenderit adipisicing incididunt eiusmod mollit reprehenderit ex minim.",
    "october": "Qui occaecat mollit reprehenderit adipisicing incididunt eiusmod mollit reprehenderit ex minim.",
    "november": "Qui occaecat mollit reprehenderit adipisicing incididunt eiusmod mollit reprehenderit ex minim.",
    "december": "Qui occaecat mollit reprehenderit adipisicing incididunt eiusmod mollit reprehenderit ex minim."
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    

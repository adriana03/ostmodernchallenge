from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from episodes.models import *
from reactions.models import *
from reactions.forms import *
from datetime import datetime as dt
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse 




# Create your views here.
def add_imagereaction(request,episode_id):
    if request.POST:
        try:
            episode = Episode.objects.get(id=episode_id)
            image = request.POST.get('image','')
            username = request.POST.get('name','')
            created_at = dt.now() 
            image =  request.FILES['image']
            image_reaction = ImageReaction.objects.create(episode=episode,image=image,created_at=created_at, username=username)
            image_reaction.save()

            return HttpResponseRedirect(reverse('episode', kwargs={'episode_id':episode.pk}))
        
        except ObjectDoesNotExist:
            raise Http404


def add_tweetreaction(request,episode_id):
    if request.POST:
        try:
            episode = Episode.objects.get(id=episode_id)
            tweet = request.POST.get('tweet','')
            username = request.POST.get('name','')
            created_at = dt.now()
            tweet_reaction = TweetReaction.objects.create(episode=episode,text=tweet,created_at=created_at, username=username)
            tweet_reaction.save()
           
            return HttpResponseRedirect(reverse('episode', kwargs={'episode_id':episode.pk}))
        
        except ObjectDoesNotExist:
            raise Http404


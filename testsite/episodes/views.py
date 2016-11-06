from django.shortcuts import render, render_to_response
from django.template import RequestContext
from reactions.models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def home(request):
    episodes = Episode.objects.all().order_by('episode_number')
    dictionary = {
        'episodes': episodes,
    }
    return render_to_response('home.html', dictionary, context_instance=RequestContext(request))

def episode(request, episode_id):
    try:
        episode = Episode.objects.get(id=episode_id)
    except ObjectDoesNotExist:
        raise Http404

    image_reactions = ImageReaction.objects.filter(episode=episode).order_by('-id')
    tweet_reactions = TweetReaction.objects.filter(episode=episode).order_by('-id')
    
    if image_reactions or tweet_reactions:
        dictionary = {
            'page_title': 'Episode',
            'episode': episode,
            'image_reactions':image_reactions,
            'tweet_reactions':tweet_reactions,
        }
    else:
        dictionary = {
            'page_title': 'Episode',
            'episode': episode,
        }

    return render_to_response('episode-single.html', dictionary, context_instance=RequestContext(request))



    
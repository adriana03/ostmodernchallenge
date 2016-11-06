from django.core.management import BaseCommand
import psycopg2
from episodes.models import *
from reactions.models import *

    #The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help

    # A command must define handle()
    def handle(self, *args, **options):
        f = open('media/episodes.xml', 'w')
        f.write('<?xml version="1.0" ?>\n')
        f.write('<mydata>\n')
        episodes = Episode.objects.all()
        for e in episodes:
            f.write('  <episode>\n')
            f.write('    <id>'+str(e.id)+'</id>\n') 
            f.write('    <title>'+e.title+'</title>\n') 
            f.write('    <episode_number>'+str(e.episode_number)+'</episode_number>\n')  
            f.write('    <created_at>'+str(e.created_at)+'</created_at>\n') 
            f.write('    <hero_image>'+str(e.hero_image)+'</hero_image>\n') 
            f.write('  </episode>\n')
        f.write('</mydata>\n')
        f.close()

        f2 = open('media/reactions.xml', 'w')
        f2.write('<?xml version="1.0" ?>\n')
        f2.write('<mydata>\n')
        imagereactions = ImageReaction.objects.all()
        tweetreactions = TweetReaction.objects.all()
        
        for i in imagereactions:
            f2.write('  <imagereaction>\n')
            f2.write('    <username>'+i.username+'</username>\n') 
            f2.write('    <episode>'+str(i.episode.id)+'</episode>\n')  
            f2.write('    <allowed_reaction>'+str(i.allowed_reaction)+'</allowed_reaction>\n') 
            f2.write('    <image>'+str(i.image)+'</image>\n') 
            f2.write('  </imagereaction>\n')
        for t in tweetreactions:
            f2.write('  <tweetreaction>\n')
            f2.write('    <username>'+t.username+'</username>\n') 
            f2.write('    <episode>'+str(t.episode.id)+'</episode>\n')  
            f2.write('    <allowed_reaction>'+str(t.allowed_reaction)+'</allowed_reaction>\n') 
            f2.write('    <text>'+str(t.text)+'</text>\n') 
            f2.write('  </tweetreaction>\n')
        f2.write('</mydata>\n')
        f2.close()





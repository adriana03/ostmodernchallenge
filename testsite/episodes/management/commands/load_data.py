from django.core.management import BaseCommand
import psycopg2
from episodes.models import *
from reactions.models import *
import xml.etree.ElementTree as ET


class Command(BaseCommand):
    
    def handle(self, *args, **options):
    
        tree = ET.parse('media/episodes.xml')
        root = tree.getroot()
        for child in root:
            e_id = child.find('id').text
            title = child.find('title').text
            episode_number = child.find('episode_number').text
            created_at = child.find('created_at').text
            hero_image = child.find('hero_image').text
            e = Episode.objects.create(id=int(e_id),title=title,episode_number=episode_number,created_at=created_at,hero_image=hero_image)
            e.save()

        tree2 = ET.parse('media/reactions.xml')
        root2 = tree2.getroot()
        for child in root2:
            if child.tag == 'imagereaction':
                username = child.find('username').text
                episode = child.find('episode').text
                episode = Episode.objects.get(id=int(episode))
                allowed_reaction = child.find('allowed_reaction').text
                image = child.find('image').text
                if allowed_reaction == 'True':
                    allowed_reaction = True
                elif allowed_reaction == 'False':
                    allowed_reaction = False
                i = ImageReaction.objects.create(episode=episode,image=image,created_at=created_at, username=username,allowed_reaction=allowed_reaction)
                i.save()

            elif child.tag == 'tweetreaction':
                username = child.find('username').text
                episode = child.find('episode').text
                episode = Episode.objects.get(id=int(episode))
                allowed_reaction = child.find('allowed_reaction').text
                tweet = child.find('text').text
                if allowed_reaction == 'True':
                    allowed_reaction = True
                elif allowed_reaction == 'False':
                    allowed_reaction = False
                e = TweetReaction.objects.create(episode=episode,text=tweet,created_at=created_at, username=username,allowed_reaction=allowed_reaction)
                e.save()

                
from django.db import models
from django.contrib.auth.models import User
from episodes.models import *



class AbstractReaction(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        abstract = True


class ImageReaction(AbstractReaction):
    username = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/images', blank=True)
    episode = models.ForeignKey(Episode, blank=True, null=True) 
    allowed_reaction = models.BooleanField(default=False)



class TweetReaction(AbstractReaction):
    username = models.TextField(blank=True)
    text = models.CharField(max_length=150)
    episode = models.ForeignKey(Episode, blank=True, null=True)
    allowed_reaction = models.BooleanField(default=False)


'''

| TASK 1 |
I have updated ImageReaction and TweetReaction adding episode field as a foreign key to episode
due to each reaction should be related to a unique episode, but each episode
can have more than one reaction.

|TASK 3|

I do also add in both reaction a boolean field called allowed reaction, which would be a 0
if the reaction is allowed to be shown and would be 1 if it is not allowed to be shown.
( we cannot delete the reactions if we want to delete/undelete the reaction, so this boolean make 
it possible for admin to moderate the site. 


'''
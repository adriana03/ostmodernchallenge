from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from episodes import views as episodes
from reactions import views as reactions

from django.conf.urls import patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', episodes.home, name='home'),
    url(r'^episode/(?P<episode_id>[-\w]+)/$', episodes.episode, name='episode'),
    
    url(r'^episode/(?P<episode_id>[-\w]+)/add_imagereaction/$', reactions.add_imagereaction, name='add_imagereaction'),
    url(r'^episode/(?P<episode_id>[-\w]+)/add_tweetreaction/$', reactions.add_tweetreaction, name='add_tweetreaction'),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


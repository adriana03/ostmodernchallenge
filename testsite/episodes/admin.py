from django.contrib import admin

from .models import Episode


class EpisodeAdmin(admin.ModelAdmin):
	actions = ('export_csv', )
	
admin.site.register(Episode, EpisodeAdmin)

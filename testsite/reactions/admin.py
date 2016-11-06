from django.contrib import admin

from .models import ImageReaction, TweetReaction


class ImageReactionAdmin(admin.ModelAdmin):
    actions = ('export_csv')
    list_display = ('id', 'image', 'episode', 'allowed_reaction')
    list_filter = ('allowed_reaction', )
    search_fields = ('id', 'episode')

    def get_form(self, request, obj=None, **kwargs):
        form = super(ImageReactionAdmin, self).get_form(request, obj, **kwargs)
        return form

class TweetReactionAdmin(admin.ModelAdmin):
    actions = ('export_csv')
    list_display = ('id', 'text', 'episode', 'allowed_reaction')
    list_filter = ('allowed_reaction', )
    search_fields = ('id', 'episode')

    def get_form(self, request, obj=None, **kwargs):
        form = super(TweetReactionAdmin, self).get_form(request, obj, **kwargs)
        return form


admin.site.register(ImageReaction, ImageReactionAdmin)
admin.site.register(TweetReaction, TweetReactionAdmin)



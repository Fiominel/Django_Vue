from django.contrib import admin
from .models import *
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_date', 'site', 'trailer', 'url')


admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Developer)
admin.site.register(Game, GameAdmin)
admin.site.register(GameScreenShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Review)
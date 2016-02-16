from django.contrib import admin
from chooser.models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'min_players',
        'max_players',
    )

admin.site.register(Game, GameAdmin)

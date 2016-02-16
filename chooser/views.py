from django.shortcuts import render
from django.http import HttpResponse

from random import choice

from chooser.models import Game

def get_random_game(request):
    num_players = int(request.GET['num_players'])

    games = Game.objects.filter(
        min_players__gte=num_players,
        max_players__lte=num_players,
    )

    if len(games) == 0:
        return HttpResponse('No games found for ' + num_players + ' players.')

    game = choice(games)

    return HttpResponse('You are playing: ' + game.name)

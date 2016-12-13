from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime, timedelta
from random import choice, randint, seed
import hashlib
import urllib2

from chooser.models import Game

def get_random_game(request):
    if 'num_players' not in request.GET:
        return HttpResponse('You need to set the num_players URL parameter. (now hiring UX designers!)')

    num_players = int(request.GET['num_players'])

    games = Game.objects.filter(
        min_players__lte=num_players,
        max_players__gte=num_players,
    )

    if len(games) == 0:
        return HttpResponse(
          'No games found for ' + str(num_players) + ' players.'
        )

    game = choice(games)

    return HttpResponse('You are playing: ' + game.name)

def get_random_page(request):
    given_date = datetime.strptime(request.GET['date'], '%Y-%m-%d')
    date_minus_one = given_date - timedelta(days=1)
    new_date = date_minus_one.strftime('%Y-%m-%d')

    weather_url = 'https://api.weathersource.com/v1/3edbb6e33559dbd9bee9/history_by_postal_code.json?period=day&postal_code_eq=94065&country_eq=US&timestamp_eq=%sT00:00:00-07:00&fields=postal_code,country,timestamp,tempMax,tempAvg,tempMin,precip,snowfall,windSpdMax,windSpdAvg,windSpdMin,cldCvrMax' % (new_date)

    weather_json = urllib2.urlopen(weather_url).read()

    if len(weather_json) < 10:
        return HttpResponse('Sorry, can\'t predict that date yet.')

    if 'count' in request.GET:
        count = request.GET['count']

        if count != '1':
            weather_json = weather_json + '_' + count

    weather_hash = int(hashlib.sha1(weather_json).hexdigest(), 16) % (10 ** 10)
    seed(weather_hash)

    return HttpResponse(
      'Your page for today is: %d.\n\n<!-- Weather hash: %s -->' % (
        (randint(1, 365)),
        weather_hash,
      )
    )

@csrf_exempt
def escape(request):
    if request.method == "POST":
        first = request.POST['first']
        second = request.POST['second']
        third = request.POST['third']

        all = sorted([first.lower(), second.lower(), third.lower()])

        if all == ['cactus', 'pumpkin', 'traktor']:
            template = """
            <img src="http://i.imgur.com/nfvQ5ss.jpg" />
            """

            return HttpResponse(template)

        return HttpResponse('Nope.')

    template = """
<!-- Death gives meaning to our lives. It gives importance and value to time. Time would become meaningless if there were too much of it. -->

<form method="POST">
Don't forget! Once someone leaves a quarantine zone they won't be allowed to reenter (for reasons of public safety, of course).

<br />
<br />

Also, they have 30 minutes left to live. No big deal.

<br />
<br />

  <input type="text" name="first">
  <br>
  <br>

  <input type="text" name="second">
  <br>
  <br>

  <input type="text" name="third">
  <br>
  <br>

  <input type="submit" value="Submit">
</form>
    """

    return HttpResponse(template)

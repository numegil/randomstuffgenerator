from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255, unique=True)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    picture = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

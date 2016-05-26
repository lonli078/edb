from __future__ import unicode_literals

from django.db import models

"""
{u'alliances': {u'href': u'https://crest-tq.eveonline.com/alliances/'},
 u'authEndpoint': {u'href': u'https://login-tq.eveonline.com/oauth/token/'},
 u'battleTheatres': {u'href': u'https://crest-tq.eveonline.com/battles/theatres/'},
 u'bloodlines': {u'href': u'https://crest-tq.eveonline.com/bloodlines/'},
 u'channels': {u'href': u'https://crest-tq.eveonline.com/chat/channels/'},
 u'clients': {u'dust': {u'href': u'https://crest-tq.eveonline.com/roots/dust/'},
              u'eve': {u'href': u'https://crest-tq.eveonline.com/roots/eve/'}},
 u'constellations': {u'href': u'https://crest-tq.eveonline.com/constellations/'},
 u'corporationRoles': {u'href': u'https://crest-tq.eveonline.com/corporations/roles/'},
 u'corporations': {u'href': u'https://crest-tq.eveonline.com/corporations/'},
 u'crestEndpoint': {u'href': u'https://crest-tq.eveonline.com/'},
 u'decode': {u'href': u'https://crest-tq.eveonline.com/decode/'},
 u'dogma': {u'attributes': {u'href': u'https://crest-tq.eveonline.com/dogma/attributes/'},
            u'effects': {u'href': u'https://crest-tq.eveonline.com/dogma/effects/'}},
 u'incursions': {u'href': u'https://crest-tq.eveonline.com/incursions/'},
 u'industry': {u'facilities': {u'href': u'https://crest-tq.eveonline.com/industry/facilities/'},
               u'systems': {u'href': u'https://crest-tq.eveonline.com/industry/systems/'}},
 u'insurancePrices': {u'href': u'https://crest-tq.eveonline.com/insuranceprices/'},
 u'itemCategories': {u'href': u'https://crest-tq.eveonline.com/inventory/categories/'},
 u'itemGroups': {u'href': u'https://crest-tq.eveonline.com/inventory/groups/'},
 u'itemTypes': {u'href': u'https://crest-tq.eveonline.com/types/'},
 u'map': {u'href': u'https://crest-tq.eveonline.com/map/'},
 u'marketGroups': {u'href': u'https://crest-tq.eveonline.com/market/groups/'},
 u'marketPrices': {u'href': u'https://crest-tq.eveonline.com/market/prices/'},
 u'marketTypes': {u'href': u'https://crest-tq.eveonline.com/market/types/'},
 u'motd': {u'dust': {u'href': u'http://newsfeed.eveonline.com/articles/71'},
           u'eve': {u'href': u'http://client.eveonline.com/motd/'},
           u'server': {u'href': u'http://client.eveonline.com/motd/'}},
 u'npcCorporations': {u'href': u'https://crest-tq.eveonline.com/corporations/npccorps/'},
 u'opportunities': {u'groups': {u'href': u'https://crest-tq.eveonline.com/opportunities/groups/'},
                    u'tasks': {u'href': u'https://crest-tq.eveonline.com/opportunities/tasks/'}},
 u'races': {u'href': u'https://crest-tq.eveonline.com/races/'},
 u'regions': {u'href': u'https://crest-tq.eveonline.com/regions/'},
 u'serverName': u'TRANQUILITY',
 u'serverVersion': u'EVE-TRANQUILITY 14.04.1036506.1036504',
 u'serviceStatus': {u'dust': u'online',
                    u'eve': u'online',
                    u'server': u'online'},
 u'sovereignty': {u'campaigns': {u'href': u'https://crest-tq.eveonline.com/sovereignty/campaigns/'},
                  u'structures': {u'href': u'https://crest-tq.eveonline.com/sovereignty/structures/'}},
 u'systems': {u'href': u'https://crest-tq.eveonline.com/solarsystems/'},
 u'time': {u'href': u'https://crest-tq.eveonline.com/time/'},
 u'tournaments': {u'href': u'https://crest-tq.eveonline.com/tournaments/'},
 u'userCounts': {u'dust': 363,
                 u'dust_str': u'363',
                 u'eve': 18845,
                 u'eve_str': u'18845'},
 u'virtualGoodStore': {u'href': u'https://vgs-tq.eveonline.com/'},
 u'wars': {u'href': u'https://crest-tq.eveonline.com/wars/'}}
 """


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    href = models.CharField(max_length=255)
    name = models.CharField(max_length=30)
    last_update = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    href = models.CharField(max_length=255)
    name = models.CharField(max_length=30)
    categoria = models.ForeignKey('items.Categories', null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import json
import pycrest
from items.models import Categories
from items.models import Group


def getAllItems(page):
    ret = page().items
    while hasattr(page(), 'next'):
        page = page().next()
        ret.extend(page().items)
    return ret


class Command(BaseCommand):

    def handle(self, *args, **options):
        eve = pycrest.EVE()
        eve()
        for i in eve.itemCategories().items:
            print i
            obj, created = Categories.objects.get_or_create(id=i.id, href=i.href, name=i.name)
            print obj, created
            for g in i().groups:
                print g
                #gr, created = Group.objects.get_or_create(id=g.id, href=g.href, name=g.name, categoria=obj)
                gr, created = Group.objects.get_or_create(id=g.id)
                gr.href = g.href
                gr.name = g.name
                gr.categoria = obj
                gr.save()
                print gr, created


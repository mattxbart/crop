from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import sys
import csv

from crop.models import *

class Command(BaseCommand):
    args = '<file>'
    help = 'initial import'

    def handle(self, *args, **options):
        filename = args[0]
        data = csv.reader(open(filename))
        data.next()
        for name, number, acres in data:
            print (name)
            obj, created = Field.objects.get_or_create(name=name,
                                                       number=number,
                                                       acres=acres)


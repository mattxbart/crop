from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import sys, os
import csv
from dateutil.parser import parse
from crop.models import *
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class Command(BaseCommand):
    help = 'initial import'

    def load_fields(self):

        filename = os.path.join(BASE_DIR, '../import_data/fields.csv')
        data = csv.reader(open(filename))
        data.next()
        print ('loading fields')
        for name, number, acres in data:
            obj, created = Field.objects.get_or_create(name=name,
                                                       number=number,
                                                       acres=acres)
    def load_corn(self):

        filename = os.path.join(BASE_DIR, '../import_data/corn_milo_yields.csv')
        data = csv.reader(open(filename))
        data.next()
        print ('loading corn yields')
        for crop_type, property_name, property_number, plant_date, harvest_date, tons, moisture, seeds, kernels in data:
            crop_type, created = CropType.objects.get_or_create(name=crop_type)
            print (property_name, property_number)
            field = Field.objects.get(name=property_name, number=property_number)

            plant_date = parse(plant_date)
            harvest_date = parse(harvest_date)

            obj, created = CornMilo.objects.get_or_create(type=crop_type,
                                                          field=field,
                                                          plant_date=plant_date,
                                                          harvest_date=harvest_date,
                                                          crop_yield=tons,
                                                          moisture=moisture,
                                                          seeds=seeds,
                                                          kernels=kernels)
            print (obj)

    def handle(self, *args, **options):

        self.load_fields()
        self.load_corn()


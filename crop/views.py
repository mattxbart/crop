import csv
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from crop.models import *

def download_crops(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="crops.csv"'

    writer = csv.writer(response)
    writer.writerow(['Crop',
                     'Type',
                     'ID',
                     'Variety', 
                     'Property', 
                     'Field Number',
                     'Acres',
                     'Plant Date', 
                     'Harvest Date', 
                     'Seeds',
                     'Kernels',
                     'Moisture',
                     'Total Yield - tons', 
                     'Yield - tons per acre',
                     'Total Yield at 70%',
                     'Yield - tons per acre at 70%',])
    for obj in Crop.objects.all().select_subclasses():
        ct = ContentType.objects.get_for_model(obj)
        writer.writerow([obj.type.name,
                         ct.model,
                         obj.id,
                         obj.type.variety,
                         obj.field.name,
                         obj.field.number,
                         obj.field.acres,
                         obj.plant_date,
                         obj.harvest_date,
                         obj.moisture,
                         obj.crop_yield,
                         obj.yield_per_acre(),
                         obj.crop_yield_70(),
                         obj.yield_per_acre_70(),
                         ])

    return response

def download_amendments(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="amendments.csv"'

    writer = csv.writer(response)
    writer.writerow(['Crop',
                     'Type',
                     'ID',
                     'Date Applied',
                     'Tons',
                     'Gypsum',
                     'Sulfur',
                     'Manure',
                     ])

    for obj in Amendment.objects.all():
        ct = ContentType.objects.get_for_model(obj.crop)
        writer.writerow([obj.type.name,
                         ct.model,
                         obj.crop.id,
                         obj.date_applied,
                         obj.tons,
                         obj.amendment_ratio.gypsum,
                         obj.amendment_ratio.sulfur,
                         obj.amendment_ratio.manure,
                         ])

    return response

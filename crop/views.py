import csv
from django.http import HttpResponse
from crop.models import *

def download_corn_milo(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="corn_milo.csv"'

    writer = csv.writer(response)
    writer.writerow(['Crop', 
                     'Variety', 
                     'Property', 
                     'Number',
                     'Acres',
                     'Plant Date', 
                     'Harvest Date', 
                     'Yield', 
                     'Moisture',
                     'Seeds',
                     'Kernels',
                     'Yield (tons at 70% moisture)',
                     'Yield (tons per Acre)',
                     'Tons per Acre at 70%',])
    for obj in CornMilo.objects.all():
        writer.writerow([obj.type.name,
                         obj.type.variety,
                         obj.field.name,
                         obj.field.number,
                         obj.field.acres,
                         obj.plant_date,
                         obj.harvest_date,
                         obj.crop_yield,
                         obj.moisture,
                         obj.seeds,
                         obj.kernels,
                         obj.crop_yield_70(),
                         obj.yield_per_acre(),
                         obj.yield_per_acre_70(),
                         ])

    return response

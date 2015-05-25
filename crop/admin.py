from django.contrib import admin
from crop.models import *

class AmendmentAdmin(admin.ModelAdmin):
    related_lookup_fields = {
        'generic': [['crop_type', 'crop_id']]
    }


class AmendmentTypeAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass

class FieldAdmin(admin.ModelAdmin):
    pass

class CropTypeAdmin(admin.ModelAdmin):
    pass

class HarvestMethodAdmin(admin.ModelAdmin):
    pass

class CornMiloAdmin(admin.ModelAdmin):
    list_display = ['type', 'field', 'plant_date', 
                    'harvest_date', 'crop_yield',
                    'yield_per_acre', 'crop_yield_70',
                    'yield_per_acre_70',]

admin.site.register(Amendment, AmendmentAdmin)
admin.site.register(AmendmentType, AmendmentTypeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(CropType, CropTypeAdmin)
admin.site.register(HarvestMethod, HarvestMethodAdmin)
admin.site.register(CornMilo, CornMiloAdmin)

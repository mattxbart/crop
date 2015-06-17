from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from crop.models import *

class AmendmentAdmin(admin.ModelAdmin):
    related_lookup_fields = {
        'generic': [['crop_type', 'crop_id']]
    }
    list_display = ['application_rate', 'date_applied', 'tons']
    readonly_fields=('id',)

class AmendmentInline(GenericTabularInline):
    model = Amendment
    ct_field = 'crop_type'
    ct_fk_field = 'crop_id'

class ApplicationRateAdmin(admin.ModelAdmin):
    list_display = ['gypsum', 'manure', 'sulfur']
    readonly_fields=('id',)

class CustomerAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

class FieldAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

class CropTypeAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

class HarvestMethodAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

class CornAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
    list_display = ['type', 'field', 'plant_date', 
                    'harvest_date', 'crop_yield',
                    'yield_per_acre', 'crop_yield_70',
                    'yield_per_acre_70',]
    inlines = [AmendmentInline]

class MiloAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
    list_display = ['type', 'field', 'plant_date', 
                    'harvest_date', 'crop_yield',
                    'yield_per_acre', 'crop_yield_70',
                    'yield_per_acre_70',]
    inlines = [AmendmentInline]

class AlmondAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
    list_display = ['type', 'field', 'plant_date', 
                    'harvest_date', 'crop_yield',
                    'yield_per_acre', 'crop_yield_70',
                    'yield_per_acre_70',]
    inlines = [AmendmentInline]

admin.site.register(Amendment, AmendmentAdmin)
admin.site.register(ApplicationRate, ApplicationRateAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(CropType, CropTypeAdmin)
admin.site.register(HarvestMethod, HarvestMethodAdmin)
admin.site.register(Corn, CornAdmin)
admin.site.register(Milo, MiloAdmin)
admin.site.register(Almond, AlmondAdmin)

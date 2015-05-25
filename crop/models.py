from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class AmendmentType(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Customer(models.Model):

    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Field(models.Model):

    customer = models.ForeignKey('crop.Customer', null=True)
    name = models.CharField(max_length=255)
    number = models.CharField(verbose_name="Field Number", max_length=255)
    acres = models.FloatField()

    class Meta:
        ordering = ('name', 'number',)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.number)

class CropType(models.Model):

    name = models.CharField(max_length=255, unique=True)
    variety = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        if self.variety:
            return "{0} {1}".format(self.name, self.variety)
        return "{0}".format(self.name)

class HarvestMethod(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class CropBase(models.Model):

    type = models.ForeignKey('crop.CropType')
    field = models.ForeignKey('crop.Field')
    plant_date = models.DateField()
    harvest_date = models.DateField(null=True, blank=True)
    crop_yield = models.FloatField(verbose_name="Total Yield - tons")
    moisture = models.FloatField(help_text="Moisture - pct.")

    class Meta:
        abstract = True

class Alfalfa(CropBase):

    cutting = models.PositiveIntegerField()
    cut_date = models.DateField()
    pickup_date = models.DateField(null=True, blank=True)
    harvest_method = models.ForeignKey('crop.HarvestMethod')
    weed_spray = models.DateField(null=True, blank=True)
    first_water = models.DateField(null=True, blank=True)
    second_water = models.DateField(null=True, blank=True)
    
class CornMilo(CropBase):

    seeds = models.FloatField(help_text="lbs. per acre")
    kernels = models.FloatField(help_text="lbs. per acre")

    def crop_yield_70(self):
        return (100.0 - self.moisture) * self.crop_yield / 30.0
    crop_yield_70.short_description = 'Total Yield at 70%'

    def yield_per_acre(self):
        return self.crop_yield / self.field.acres
    yield_per_acre.short_description = 'Yield - tons per acre'

    def yield_per_acre_70(self):
        return self.crop_yield_70() / self.field.acres
    yield_per_acre_70.short_description = 'Yield - tons per acre at 70%'

    def __str__(self):
        return "{0} {1}".format(self.type, self.field)

    class Meta:
        verbose_name_plural = "Corn & Milo"

class Amendment(models.Model):

    amendment_type = models.ForeignKey('crop.AmendmentType')

    limit = models.Q(app_label = 'crop', model = 'cornmilo') | models.Q(app_label = 'crop', model = 'alfalfa')

    crop_type = models.ForeignKey(ContentType, limit_choices_to=limit)
    crop_id = models.PositiveIntegerField()
    crop = generic.GenericForeignKey("crop_type", "crop_id")
    date_applied = models.DateField()
    tons = models.FloatField()

    def __str__(self):
        return "{0} - {1}".format(self.amendment_type.name, self.crop)
    

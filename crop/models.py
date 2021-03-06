from django.db import models
from django import forms
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.validators import ValidationError
from model_utils.managers import InheritanceManager

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

class Crop(models.Model):

    type = models.ForeignKey('crop.CropType')
    field = models.ForeignKey('crop.Field')
    plant_date = models.DateField(null=True, blank=True)
    harvest_date = models.DateField(null=True, blank=True)
    crop_yield = models.FloatField(null=True, blank=True, verbose_name="Total Yield - tons")
    moisture = models.FloatField(null=True, blank=True, help_text="Moisture - pct.")

    objects = InheritanceManager()

    def crop_yield_70(self):
        try:
            return round((100.0 - self.moisture) * self.crop_yield / 30.0, 1)
        except TypeError:
            return 0.0
    crop_yield_70.short_description = 'Total Yield at 70%'

    def yield_per_acre(self):
        try:
            return round(self.crop_yield / self.field.acres, 1)
        except TypeError:
            return 0.0
    yield_per_acre.short_description = 'Yield - tons per acre'

    def yield_per_acre_70(self):
        try:
            return round(self.crop_yield_70() / self.field.acres, 1)
        except TypeError:
            return 0.0
    yield_per_acre_70.short_description = 'Yield - tons per acre at 70%'

    def __str__(self):
        return "{0} {1}".format(self.type, self.field)


class Alfalfa(Crop):

    cutting = models.PositiveIntegerField(null=True, blank=True)
    cut_date = models.DateField(null=True, blank=True)
    pickup_date = models.DateField(null=True, blank=True)
    harvest_method = models.ForeignKey('crop.HarvestMethod', null=True, blank=True)
    weed_spray = models.DateField(null=True, blank=True)
    first_water = models.DateField(null=True, blank=True)
    second_water = models.DateField(null=True, blank=True)
    
class Corn(Crop):

    seeds = models.FloatField(help_text="lbs. per acre", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Corn"

class Milo(Crop):

    kernels = models.FloatField(help_text="lbs. per acre", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Milo"

class Almond(Crop):
    pass

class ApplicationRate(models.Model):

    gypsum = models.FloatField()
    manure = models.FloatField()
    sulfur = models.FloatField()

    def clean(self, *args, **kwargs):

        qs = self.__class__._default_manager.filter(
            gypsum=self.gypsum,
            manure=self.manure,
            sulfur=self.sulfur,
        )

        if qs.exists():
            raise ValidationError(['This amendment ratio already exists',])

        super(AmendmentRatio, self).validate_unique(*args, **kwargs)

    @property
    def display_ratio(self):
        return "G {0} - M {1} - S {2}".format(self.gypsum, self.manure, self.sulfur)

    def __str__(self):
        return self.display_ratio

class Amendment(models.Model):

    application_rate = models.ForeignKey('crop.ApplicationRate')

    limit = models.Q(app_label = 'crop', model = 'corn') | models.Q(app_label = 'crop', model = 'alfalfa') | models.Q(app_label = 'crop', model = 'milo')

    crop_type = models.ForeignKey(ContentType, limit_choices_to=limit)
    crop_id = models.PositiveIntegerField()
    crop = generic.GenericForeignKey("crop_type", "crop_id")
    date_applied = models.DateField()
    tons = models.FloatField()

    def __str__(self):
        return "{0} - {1}".format(self.application_rate, self.crop)
    

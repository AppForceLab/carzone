from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.car_photo.url))
    thumbnail.short_description = "Car Image"

    list_display = ('id', 'thumbnail', 'car_title', 'model', 'city', 'color',
                    'year', 'body_stile', 'fuel_type', 'is_features')
    list_display_links = ('id', 'thumbnail', 'car_title', )
    list_editable = ('is_features',)
    search_fields = ('id', 'car_title', 'model', 'city', 'year', 'body_stile',)
    list_filter = ('model', 'city', 'year', 'body_stile',)


admin.site.register(Car, CarAdmin)

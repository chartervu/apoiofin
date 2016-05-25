from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from models import Club, Detail, Organ

class AdminClub(ModelAdmin):
    list_display = ('name','usuario')

class AdminDetail(ModelAdmin):
    list_display = ('club','address','postal_code','phones','mobiles',
        'email','tax_number','statute','util_pub','up_date','observations')

class AdminOrgan(ModelAdmin):
    list_display = ('club','president','secretary','treasurer','election','end','ontime','arrears')

admin.site.register(Club, AdminClub)
admin.site.register(Detail, AdminDetail)
admin.site.register(Organ, AdminOrgan)

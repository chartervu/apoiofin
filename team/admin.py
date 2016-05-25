from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from models import Modal, Team

class AdminTeam(ModelAdmin):
    list_display = ('name','age','sex','level','coach',)

admin.site.register(Modal)
admin.site.register(Team, AdminTeam)
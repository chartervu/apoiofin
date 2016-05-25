from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from models import Budget

class AdminBudget(ModelAdmin):
    list_display = ('club','tot_exp','facilities','activities',
        'other_activities','other_expend','expend_invest','total_rev',
        'rev_fees','rev_sponsor','other_revs','rev_subsidies')

admin.site.register(Budget, AdminBudget)
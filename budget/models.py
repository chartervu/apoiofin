# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ModelForm

from ident.models import Club

class Budget(models.Model):
    class Meta:
        ordering = ('club',)
    club = models.ForeignKey(Club)
    tot_exp = models.IntegerField()
    facilities = models.IntegerField()
    activities = models.IntegerField()
    other_activities = models.IntegerField()
    other_expend = models.IntegerField()
    expend_invest = models.IntegerField()
    total_rev = models.IntegerField()
    rev_fees = models.IntegerField()
    rev_sponsor = models.IntegerField()
    other_revs = models.IntegerField()
    rev_subsidies = models.IntegerField()

    def __unicode__(self):
        return u'%s'%(self.club)

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        #exclude = ['club']

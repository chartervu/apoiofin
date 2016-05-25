# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm

from ident.models import Club

class Modal(models.Model):
    name = models.CharField(max_length=32,unique=True,blank=False)

    def __unicode__(self):
        return'%s'%(self.name)

TEAM_MALE = 'm'
TEAM_FEMALE = 'f'
TEAM_MIST = 'b'
TEAM_CHOICES = (
(TEAM_MALE, _('Masculino')),
(TEAM_FEMALE, _('Feminino')),
(TEAM_MIST, _('Misto')),
)

LEVEL_LOCAL = 'l'
LEVEL_REGIONAL = 'r'
LEVEL_NATIONAL = 'n'
LEVEL_CHOICES = (
(LEVEL_LOCAL, _('Local')),
(LEVEL_REGIONAL, _('Regional/Distrital')),
(LEVEL_NATIONAL, _('Nacional')),
)

class Team(models.Model):
    club = models.ForeignKey(Club)
    name = models.CharField(max_length=48, blank=True)
    modal = models.ForeignKey('Modal')
    age = models.IntegerField()
    sex = models.CharField(max_length=1,default=TEAM_MIST,choices=TEAM_CHOICES, blank=True)
    level = models.CharField(max_length=1,default=LEVEL_LOCAL,choices=LEVEL_CHOICES, blank=True)
    discipline = models.CharField(max_length=32, blank=True)
    coach = models.CharField(max_length=16, blank=True)
    coach_level = models.CharField(max_length=1, blank=True)
    course_yr = models.CharField(max_length=8, blank=True)
    results = models.CharField(max_length=128, blank=True)    

    def __unicode__(self):
        return'%s'%(self.name)

    def get_absolute_url(self):
        return '/team/%d/'%self.id

class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ['club']

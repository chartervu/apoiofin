# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Club(models.Model):
    class Meta:
        ordering = ('name',)
    name = models.CharField(max_length=128)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return '%s'%(self.name)

    def get_absolute_url(self):
        return '/club/%d/'%self.id

class Detail(models.Model):
    club = models.ForeignKey('Club')
    address = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=8, blank=True)
    phones = models.CharField(max_length=44, blank=True)
    mobiles = models.CharField(max_length=44, blank=True)
    email = models.EmailField(blank=True)
    tax_number = models.IntegerField(max_length=9)
    statute = models.CharField(max_length=42)
    util_pub = models.NullBooleanField()
    up_date = models.CharField(max_length=20, blank=True)
    observations = models.CharField(max_length=512, blank=True)

    def __unicode__(self):
        return u'%s'%(self.club)

class Organ(models.Model):
    class Meta:
        ordering = ('election','end')
    club = models.ForeignKey('Club')
    president = models.CharField(max_length=42)
    secretary = models.CharField(max_length=42)
    treasurer = models.CharField(max_length=42)
    election = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    ontime = models.CharField(max_length=5, blank=True)
    arrears = models.CharField(max_length=5, blank=True)

    def __unicode__(self):
        return u'%s'%(self.club)
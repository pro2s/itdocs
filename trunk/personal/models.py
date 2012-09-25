# -*- coding: utf-8 -*-
from django.db import models

WORK_TYPE = (
    (1, u'оплата'),
    (2, u'отгул'),
    (3, u'бесплатно'),
    (4, u'субботник'),
)

class NameProf(models.Model):
    kod = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)    
    def __unicode__(self):
        return self.name
        
class Personal(models.Model):
    tn = models.IntegerField(primary_key=True)
    ceh = models.IntegerField()
    fm = models.CharField(max_length=20)
    im = models.CharField(max_length=15)
    ot = models.CharField(max_length=15)
    uch = models.IntegerField()
    brg = models.IntegerField()
    datar = models.CharField(max_length=10)
    kodprof = models.ForeignKey(NameProf, to_field='kod')
    raz = models.IntegerField()
    p_ser = models.CharField(max_length=10)
    p_nom = models.CharField(max_length=10)
    vidan = models.CharField(max_length=30)
    strana = models.IntegerField()
    datav = models.CharField(max_length=10)
    def __unicode__(self):
        return self.fm

class WeekendWork(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=15, null=True, blank=True)
    members = models.ManyToManyField(Personal, through='PeopleToWork')
    def __unicode__(self):
        return self.date
    
class PeopleToWork(models.Model):
    personal = models.ForeignKey(Personal)
    weekend = models.ForeignKey(WeekendWork)
    work_type = models.IntegerField(choices=WORK_TYPE)

# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

PAY_TYPE = (
    (1, u'оплату'),
    (2, u'предоплату'),
)

PLAN_ITEM_TYPE = (
    (1, u'единоразово'),
    (2, u'ежемесячно'),
    (3, u'ежеквартально'),
    (4, u'ежегодно'),
    (5, u'до оплаты'),
)

class Company(models.Model):
    kod = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    adres = models.CharField(max_length=60)
    nameb = models.CharField(max_length=40)
    schet = models.CharField(max_length=20)
    mfo = models.CharField(max_length=9)
    adrb = models.CharField(max_length=40)
    strana = models.IntegerField()
    unp = models.CharField(max_length=15)
    kpp = models.CharField(max_length=15)
    desc = models.CharField(max_length=30)
    def __unicode__(self):
	return self.name

class CompanyInfo(models.Model):
    company = models.ForeignKey(Company)
    boss = models.CharField(max_length=60)
    boss_fio = models.CharField(max_length=60)
    phone = models.CharField(max_length=15, null=True, blank=True)
    fax = models.CharField(max_length=15, null=True, blank=True)
    def __unicode__(self):
	return u'%s (%s)' % (self.boss, self.company.name) 
	
class ContractType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True, blank=True)    
    formula = models.CharField(max_length=100, null=True, blank=True)
    def __unicode__(self):
	return self.name


class Contract(models.Model):
    number = models.CharField(max_length=30)
    company = models.ForeignKey(Company)
    open_date = models.DateField()
    close_date = models.DateField(null=True, blank=True)
    contract_type = models.ForeignKey(ContractType)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    def __unicode__(self):
	return u'%s от %s' % (self.number, self.open_date.strftime('%d.%m.%Y')) 

class InvoiceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __unicode__(self):
	return self.name
	
class Invoice(models.Model):
    contract = models.ForeignKey(Contract)
    number = models.CharField(max_length=30)
    sum = models.IntegerField()
    nds = models.IntegerField()
    invoice_type = models.ForeignKey(InvoiceType)     
    invoice_date = models.DateField()
    def __unicode__(self):
	return u'№ %s от %s (%s)' % (self.number, self.invoice_date.strftime('%d.%m.%Y'), self.contract.number) 
	
class RecieptType(models.Model):
    name = models.CharField(max_length=30)
    period = models.CharField(max_length=50)    
    formula = models.CharField(max_length=100)
    def __unicode__(self):
	return self.name

class Payment(models.Model):
    contract = models.ForeignKey(Contract, null=True, blank=True)
    invoices = models.ManyToManyField(Invoice, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    type = models.IntegerField( choices=PAY_TYPE)
    payment_date = models.DateField()
    sum = models.IntegerField()
    nds = models.IntegerField()
    description = models.CharField(max_length=100)    
    reciept_type = models.ForeignKey(RecieptType) 
    receipt = models.CharField(max_length=100)    
    payment_doc = models.IntegerField(null=True, blank=True)    
    user = models.ForeignKey(User)  
    def __unicode__(self):
	return u'№ %s/604 от %s' % (self.number, self.date.strftime('%d.%m.%Y')) 

class Currency(models.Model):
    name = models.CharField(max_length=50)    
    short_name = models.CharField(max_length=10)    
    kod = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.short_name
	
class PlanItem(models.Model):
    number = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=250)    
    sum = models.IntegerField()
    type = models.IntegerField(choices=PLAN_ITEM_TYPE)
    currency = models.ForeignKey(Currency, null=True, blank=True)
    def __unicode__(self):
        return self.description
        
class Plan(models.Model):
    number = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    items = models.ManyToManyField(PlanItem)
    
    
def plan_created(sender, instance, created, **kwargs):
    if created:
        #create regular items
        for item in PlanItem.objects.exclude(type=1):
            print 'the object is now saved.'
            #add items 

post_save.connect(plan_created, sender=Plan)

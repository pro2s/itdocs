# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from finances.models import Company, CompanyInfo, ContractType, Contract, InvoiceType, Invoice, RecieptType, Payment, Currency, PlanItem, Plan

#class PaymentAdminForm(forms.ModelForm):
#def __init__(self, *args, **kwargs):
#    super(PaymentAdminForm, self).__init__(*args, **kwargs)
#    if (self.instance.contract is None):
#        self.fields['invoices'].queryset = Invoice.objects.all()
#    else:
#        self.fields['invoices'].queryset = Invoice.objects.filter(contract=self.instance.contract)

class PlanItemsInline(admin.TabularInline):
    model = Plan.items.through

class PlanAdmin(admin.ModelAdmin):
    inlines = [
        PlanItemsInline,
    ]
    exclude = ('items',)

    
class PaymentInvoicesInline(admin.TabularInline):
    model = Payment.invoices.through
    
class PaymentAdmin(admin.ModelAdmin):
#    form = PaymentAdminForm
#    filter_horizontal = ('invoices',)
    inlines = [
        PaymentInvoicesInline,
    ]
    exclude = ('invoices',)
    
class CompanyAdmin(admin.ModelAdmin):
	 search_fields = ['name',]
	
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyInfo)
admin.site.register(Contract)
admin.site.register(ContractType)
admin.site.register(InvoiceType)
admin.site.register(Invoice)
admin.site.register(RecieptType)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(PlanItem)
admin.site.register(Currency)

  








from django.contrib import admin
from django import forms
from finances.models import Company, CompanyInfo, ContractType, Contract, InvoiceType, Invoice, RecieptType, Payment

class PaymentAdminForm(forms.ModelForm):
  class Meta:
    model = Payment

  def __init__(self, *args, **kwargs):
    super(PaymentAdminForm, self).__init__(*args, **kwargs)
    self.fields['invoices'].queryset = Invoice.objects.filter(contract=self.instance.contract)

  
class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForm
    filter_horizontal = ('invoices',)

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
  








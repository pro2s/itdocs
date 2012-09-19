# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import Context, loader
from finances.models import Payment
from django.shortcuts import render_to_response
from django.http import Http404

def index(request):
    return HttpResponse(u"<a href='/payments/'>Платежи</a> ")

def payments(reqyest):
    payments_list = Payment.objects.all() #.order_by('-pub_date')[:5]
    t = loader.get_template('payments/index.html')
    c = Context({
        'payments_list': payments_list,
    })
    return HttpResponse(t.render(c))
    
def payments_print(request, payment_id):
    try:
        p = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        raise Http404
    return render_to_response('payments/print.html', {'payment': p})
    
def payments_edit(request, payment_id):
    try:
        p = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        raise Http404
    return render_to_response('payments/print.html', {'payment': p})
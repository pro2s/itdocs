# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import modelformset_factory
from django.template import Context, loader
from finances.models import Payment, PaymentForm
from django.shortcuts import render_to_response, get_object_or_404
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

def payments_delete(request, payment_id):
    try:
        p = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        raise Http404
    p.delete()
    return HttpResponseRedirect("/payments/")

def payments_edit(request, payment_id = None):
    if payment_id:
        p = get_object_or_404(Payment, pk=payment_id)
    else:
        p = Payment()
    if request.method == 'POST':
        submit = request.POST.get('cancel', None)
        if submit:
            return HttpResponseRedirect("/payments/")
        else:
            formset = PaymentForm(request.POST, instance=p)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect("/payments/")
                # do something.
    else:
        formset = PaymentForm(instance=p)
    return render_to_response("payments/edit.html", {
        "formset": formset,
    })
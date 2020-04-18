from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .forms import createOrderForm
from.models import ccwOrderDetails
from .operations import operations
from .requestTemplates.requestTemplates import ccwOrderRequest


# Create your views here.

def createOrder(request):
    form=createOrderForm

    return render(request,'create_order.html',{'form':form})


def home(request):
    wid=operations.generateWebOrderId()
    return render(request,'create_order.html',{'wid':wid})


def orderData(request):
    webOrderId=operations.generateWebOrderId()
    offer=request.GET['offerName']
    Qty=request.GET['qty']
    requestedStartDate=request.GET['rsd']
    initial_term=request.GET['initialTerm']
    renewal_term=request.GET['renewalTerm']
    prov_email=request.GET['provEmail']
    deliveryMethod=operations.getDeliveryMethod(offer)


    ccwOrderDetails.objects.create(web_order_id=webOrderId,offer=offer,Quantity=Qty,initial_term=initial_term,renewal_term=renewal_term,prov_email=prov_email,deliveryMethod=deliveryMethod,requestedStartDate=requestedStartDate)
    oplrequest=ccwOrderRequest(webOrderId)
    oplSendStatus=operations.sendOrderDetailsToOpl(oplrequest)
    if oplSendStatus==True:
        oplstatus='SUCCESS'
    else:
        oplstatus='FAILURE'

    output=webOrderId

    return render(request,'order_data.html',{'out':output,'OPLPostStatus':oplstatus})



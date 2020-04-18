from ccw.models import ccwOrderDetails,offerSetupDetails
import requests

def generateWebOrderId():
    a=ccwOrderDetails.objects.all()
    b=int(a[len(a)-1].web_order_id)+1
    return str(b)

def getDeliveryMethod(offer):
    od=offerSetupDetails.objects.all()
    na='NA'
    for i in range(len(od)):
        if od[i].offer==offer:
            return od[i].deliveryMethod
    return na

def sendOrderDetailsToOpl(req):
    opl_url = 'http://localhost:7000/opl/'
    response = requests.post(url=opl_url, data=req, headers={'Content-type': 'application/json'})
    if response.status_code==201:
        return True
    return False



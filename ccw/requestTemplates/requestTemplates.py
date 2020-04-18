from ccw.models import ccwOrderDetails
import json

def ccwOrderRequest(wid):
    data=ccwOrderDetails.objects.filter(web_order_id=wid)
    d=data[0]
    def getArFlag(d):
        arFlag=False
        if d.renewal_term==0:
            arFlag=False
        else:
            arFlag=True
        return arFlag

    req={'salesOrderNo':d.web_order_id,'offerName':d.offer,'quantity':d.Quantity,'initialTerm':d.initial_term,
         'renewalTerm':d.renewal_term,'prov_email':d.prov_email,'tfEligible':d.isTfEligible,
         'deliveryMethod':d.deliveryMethod,'autoRenewalFlag':getArFlag(d),'requestedStartDate':d.requestedStartDate
         }

    class DatetimeEncoder(json.JSONEncoder):#this class is meant to serialize the date time to json format otherwise json.dumps will fail
        def default(self, obj):
            try:
                return super(DatetimeEncoder, obj).default(obj)
            except TypeError:
                return str(obj)
    reqs=json.dumps(req,cls=DatetimeEncoder)
    return reqs


from django.db import models
import uuid
from django.utils.timezone import now

# Create your models here.
class ccwOrderDetails(models.Model):
    web_order_id=models.CharField(max_length=10)
    offer=models.CharField(max_length=20)
    Quantity=models.IntegerField()
    initial_term=models.IntegerField()
    renewal_term=models.IntegerField()
    prov_email=models.EmailField()
    isTfEligible=models.BooleanField(default=True)
    deliveryMethod=models.CharField(max_length=20,default='NA')
    requestedStartDate=models.DateField(default=now())

    def __str__(self):
        return self.web_order_id

class offerSetupDetails(models.Model):
    offerId=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    offer=models.CharField(max_length=20)
    deliveryMethod=models.CharField(max_length=10)

    def __str__(self):
        return self.offer


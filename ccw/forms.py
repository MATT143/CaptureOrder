from django import forms

class createOrderForm(forms.Form):
    offer=forms.CharField()
    Quantity=forms.IntegerField()
    requestedStartDate=forms.DateField()
    initialTerm=forms.IntegerField()
    renewalTerm=forms.IntegerField()
    provisioningEmail=forms.EmailField()
    tfEligible=forms.BooleanField()
from django import forms

from vendor.models import Vendor 

class Vendorform(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name','vendor_license']
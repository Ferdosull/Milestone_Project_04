from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Creating an order form using a Meta class
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, add custom
        labels for specific fields and set
        autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields['full_name'].label = 'Full Name'
            self.fields['email'].label = 'Email Address'
            self.fields['phone_number'].label = 'Phone Number'
            self.fields['postcode'].label = 'Postal Code'
            self.fields['town_or_city'].label = 'Town or City'
            self.fields['street_address1'].label = 'Street Address 1'
            self.fields['street_address2'].label = 'Street Address 2'
            self.fields['county'].label = 'County, State or Locality'

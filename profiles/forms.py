from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Addition of placeholders and classes, add and edit
        auto generated labels and set autofocus on first field
        which is phone number.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields['default_phone_number'].label = "Phone Number"
            self.fields['default_postcode'].label = "Postal Code"
            self.fields['default_town_or_city'].label = "Town or City"
            self.fields['default_street_address1'].label = "Street Address 1"
            self.fields['default_street_address2'].label = "Street Address 2"
            self.fields['default_county'].label = "County, State or Locality"

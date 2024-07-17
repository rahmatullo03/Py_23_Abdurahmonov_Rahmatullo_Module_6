
import re

from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

from apps.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     return make_password(password)


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','email','last_name','phone_number','mobile_number')

    def clean_phone_number(self):
        phone_number = re.sub('\D', '',self.cleaned_data.get('phone_number'))
        mobile_number = re.sub('\D', '',self.cleaned_data.get('mobile_number'))
        return phone_number and mobile_number

    # def clean_phone_number(self):
    #     phone_number = re.sub('\D', '',self.cleaned_data.get('phone_number'))
    #     return phone_number

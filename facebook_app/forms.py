from . models import Log_in,Profile
from django.forms import ModelForm



class Loginform(ModelForm):
    class Meta:
        model=Log_in
        fields=["username","password"]


class Createform(ModelForm):
    class Meta:
        model = Log_in
        fields='__all__'

class Profileform(ModelForm):
    class Meta:
        model=Log_in
        exclude = ('username', 'password',)        


import django_filters

from django_filters import DateFilter , CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    note = CharFilter(field_name = 'note', lookup_expr='icontains' )



    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date_created']


class CustomerFilter(django_filters.FilterSet):
    name = CharFilter(field_name ='name', lookup_expr='icontains')
    phone = CharFilter(field_name = 'phone', lookup_expr='icontains')
    address = CharFilter(field_name= 'address', lookup_expr='icontains')




    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['email','date_created']

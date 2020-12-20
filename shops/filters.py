import datetime

from django.db.models import F, Q, Case, When
from django.db.models import Value, TimeField
from django_filters import FilterSet, NumberFilter, CharFilter

from shops.models import Shops


class ShopsFilter(FilterSet):
    open = NumberFilter(method='filter_open_or_close_shops', label='open')
    street = CharFilter(field_name='address__street__name', distinct=False, lookup_expr='icontains')
    city = CharFilter(field_name='address__street__city__name', distinct=False, lookup_expr='icontains')

    class Meta:
        model = Shops
        fields = ['open', 'street', 'city']

    def filter_open_or_close_shops(self, queryset, name, value):
        time_now = datetime.datetime.now().time()
        queryset = queryset.annotate(time_now=Value(time_now, output_field=TimeField()))
        if value == 1:
            return queryset.filter(
                Q(time_now__range=[F('time_open'),
                                   Case(When(time_open__lte=F('time_close'),
                                             then='time_close'),
                                        default=datetime.time(23, 59))]) |
                Q(time_now__range=[Case(When(time_open__lte=F('time_close'),
                                             then='time_open'),
                                        default=datetime.time(0, 0)),
                                   F('time_close')]))
        elif value == 0:
            return queryset.filter(
                Q(time_now__range=[F('time_close'),
                                   Case(When(time_open__lte=F('time_close'),
                                             then=datetime.time(23, 59)),
                                        default='time_open')]) |
                Q(time_now__range=[Case(When(time_open__lte=F('time_close'),
                                             then=datetime.time(0, 0)),
                                        default='time_open'),
                                   F('time_open')]))
        return queryset

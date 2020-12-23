from django_filters import FilterSet, OrderingFilter
from .models import Streets, Cities


class CitiesFilter(FilterSet):
    order_by_field = 'ordering'
    ordering = OrderingFilter(
        fields=(
            ('name', 'name'),
        ),
    )

    class Meta:
        model = Cities
        fields = ['name']


class StreetsFilter(FilterSet):
    order_by_field = 'ordering'
    ordering = OrderingFilter(
        fields=(
            ('name', 'name'),
            ('city__name', 'city'),
        ),
    )

    class Meta:
        model = Streets
        fields = ['name']

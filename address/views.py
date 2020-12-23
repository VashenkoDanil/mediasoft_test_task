from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from address.models import Cities
from address.serializers import CitySerializer, StreetSerializer
from shops.exceptions import check_error_and_return_bad_request
from .filters import CitiesFilter, StreetsFilter


class CitiesViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer

    filter_backends = [DjangoFilterBackend]
    filter_class = CitiesFilter

    @check_error_and_return_bad_request
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(methods=['get'], detail=True, url_path='street', url_name='list_streets')
    @check_error_and_return_bad_request
    def list_streets(self, request, pk=None):
        city = get_object_or_404(Cities, pk=pk)
        streets_filter = StreetsFilter(request.GET, city.streets_set.all())
        serializer = StreetSerializer(streets_filter.qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

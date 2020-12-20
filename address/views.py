from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from address.models import Cities
from address.serializers import CitySerializer, StreetSerializer
from shops.exceptions import check_error_and_return_bad_request


class CitiesViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

    @check_error_and_return_bad_request
    def list(self, request, *args, **kwargs):
        return super(CitiesViewSet, self).list(request, *args, **kwargs)

    @action(methods=['get'], detail=True, url_path='street', url_name='list_streets')
    def list_streets(self, request, pk=None):
        try:
            streets = self.get_object().streets_set.all()
            serializer = StreetSerializer(streets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

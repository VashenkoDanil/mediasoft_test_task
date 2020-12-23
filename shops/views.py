from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .exceptions import check_error_and_return_bad_request
from .filters import ShopsFilter
from .models import Shops
from .serializers import ShopSerializer


class ShopsViewSet(ListModelMixin, GenericViewSet):
    queryset = Shops.objects.all()
    serializer_class = ShopSerializer

    filter_backends = [DjangoFilterBackend]
    filter_class = ShopsFilter

    @check_error_and_return_bad_request
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @check_error_and_return_bad_request
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data.get('id'), status=status.HTTP_200_OK)

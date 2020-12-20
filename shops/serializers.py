from rest_framework import serializers

from .exceptions import ShopWithThisNameAndAddressAlreadyExistsError
from .models import Shops
from address.serializers import AddressSerializer


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='address.street.city.name')
    street = serializers.CharField(source='address.street.name')
    house = serializers.CharField(source='address.house')
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Shops
        fields = ['id', 'name', 'city', 'street', 'house', 'time_open', 'time_close']

    def create(self, validated_data):
        address = self._get_or_create_address(validated_data)
        validated_data['address_id'] = address.id
        return self._create_shop(validated_data)

    def _create_shop(self, validated_data):
        try:
            Shops.objects.get(**validated_data)
            raise ShopWithThisNameAndAddressAlreadyExistsError()
        except Shops.DoesNotExist:
            return super(ShopSerializer, self).create(validated_data)

    def _get_or_create_address(self, validated_data):
        address = validated_data.pop('address')
        address_serializer = AddressSerializer(data=address)
        address_serializer.is_valid(raise_exception=True)
        return address_serializer.save()

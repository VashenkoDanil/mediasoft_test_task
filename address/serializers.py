from rest_framework import serializers

from .models import Cities, Streets, Address


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['name']

    def create(self, validated_data):
        name_city = validated_data.get('name')
        city, _ = Cities.objects.get_or_create(name=name_city)
        return city


class StreetSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False, write_only=True)

    class Meta:
        model = Streets
        fields = ['name', 'city']

    def create(self, validated_data):
        city = self._get_or_create_city(validated_data)
        validated_data['city_id'] = city.id
        return self._get_or_create_street(validated_data)

    def _get_or_create_street(self, validated_data):
        try:
            return Streets.objects.get(**validated_data)
        except Streets.DoesNotExist:
            return super(StreetSerializer, self).create(validated_data)

    def _get_or_create_city(self, validated_data):
        city = validated_data.pop('city')
        city_serializer = CitySerializer(data=city)
        city_serializer.is_valid(raise_exception=True)
        return city_serializer.save()


class AddressSerializer(serializers.ModelSerializer):
    street = StreetSerializer(many=False, write_only=True)

    class Meta:
        model = Address
        fields = ['street', 'house']

    def create(self, validated_data):
        street = self._get_or_create_street(validated_data)
        validated_data['street_id'] = street.id
        return self._get_or_create_address(validated_data)

    def _get_or_create_address(self, validated_data):
        try:
            return Address.objects.get(**validated_data)
        except Address.DoesNotExist:
            return super(AddressSerializer, self).create(validated_data)

    def _get_or_create_street(self, validated_data):
        street = validated_data.pop('street')
        street_serializer = StreetSerializer(data=street)
        street_serializer.is_valid(raise_exception=True)
        return street_serializer.save()

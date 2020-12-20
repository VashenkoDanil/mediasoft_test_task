from django.db import models


class Cities(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Streets(models.Model):
    name = models.CharField(max_length=256)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return f'Город: {self.city.name}, Улица: {self.name}'


class Address(models.Model):
    street = models.ForeignKey(Streets, on_delete=models.CASCADE)
    house = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.street}, Дом: {self.house}'

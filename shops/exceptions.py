from rest_framework import status
from rest_framework.response import Response


class ShopWithThisNameAndAddressAlreadyExistsError(Exception):
    """Магазин с таким именем и адресом уже существует"""

    def __init__(self, message='Магазин с таким именем и адресом уже существует'):
        self.message = message
        super().__init__(self.message)


def check_error_and_return_bad_request(func):
    """Декоратор для обработки ошибок, методы должны возвращать либо ответ 200 либо 400"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return wrapper

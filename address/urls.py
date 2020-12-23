from rest_framework import routers
from .views import CitiesViewSet

router = routers.SimpleRouter()

router.register(r'', CitiesViewSet, basename='city')

urlpatterns = router.urls

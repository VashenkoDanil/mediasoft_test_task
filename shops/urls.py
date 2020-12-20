from rest_framework import routers
from .views import ShopsViewSet

router = routers.SimpleRouter()

router.register(r'', ShopsViewSet)

urlpatterns = router.urls

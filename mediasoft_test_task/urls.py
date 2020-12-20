from django.contrib import admin
from django.urls import path, include
from django.views import defaults


handler403 = defaults.bad_request
handler404 = defaults.bad_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('city/', include('address.urls')),
    path('shop/', include('shops.urls')),
]

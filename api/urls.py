from django.urls import path, include
from .views import QuakeGenericViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('quakes', QuakeGenericViewSet, basename='quakes')

urlpatterns = [
    path('', include(router.urls)),
]
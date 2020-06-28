from django.urls import path, include
from cats.views import CatsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cats', CatsViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

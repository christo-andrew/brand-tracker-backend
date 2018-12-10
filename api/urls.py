from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'places', views.PlaceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', csrf_exempt(views.LoginView.as_view())),
]

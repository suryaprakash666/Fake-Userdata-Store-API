from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Userdata_api.views import Dataviewset

router = DefaultRouter()
router.register(r'dataview', Dataviewset)
from Userdata_api import UserRegistrationView

urlpatterns = [
    path('', include(router.urls)),
]

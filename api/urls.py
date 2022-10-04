from django . urls import path,include
from rest_framework import routers
from .views import Customerviewset

router = routers.DefaultRouter()
router.register (r"customers",Customerviewset)

urlpatterns = [
    path("",include(router.urls)),
]
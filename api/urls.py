from django . urls import path,include
from rest_framework import routers
from .views import Customerviewset
from .views import Accountviewset,Transactionviewset,Loanviewset,Receiptviewset,Notificationviewset,Rewardviewset,Currencyviewset,Cardviewset,Thirdpartyviewset,Walletviewset

router = routers.DefaultRouter()
router.register (r"customers",Customerviewset)

urlpatterns = [
    path("",include(router.urls)),
]


router = routers.DefaultRouter()
router.register (r"accounts",Accountviewset)

urlpatterns = [
    path("",include(router.urls)),
]


router = routers.DefaultRouter()
router.register (r"transactions",Transactionviewset)

urlpatterns = [
    path("",include(router.urls)),
]

router = routers.DefaultRouter()
router.register (r"loans",Loanviewset)

urlpatterns = [
    path("",include(router.urls)),
]
router = routers.DefaultRouter()
router.register (r"receipts",Receiptviewset)

urlpatterns = [
    path("",include(router.urls)),
]

router = routers.DefaultRouter()
router.register (r"notifications",Notificationviewset)

urlpatterns = [
    path("",include(router.urls)),
]

router = routers.DefaultRouter()
router.register (r"rewards",Rewardviewset)

urlpatterns = [
    path("",include(router.urls)),
]

router = routers.DefaultRouter()
router.register (r"currency",Currencyviewset)

urlpatterns = [
    path("",include(router.urls)),
]

router = routers.DefaultRouter()
router.register (r"cards",Currencyviewset)

urlpatterns = [
    path("",include(router.urls)),
]

router = routers.DefaultRouter()
router.register (r"thirdparty",Currencyviewset)

urlpatterns = [
    path("",include(router.urls)),
]

router = routers.DefaultRouter()
router.register (r"wallet",Currencyviewset)

urlpatterns = [
    path("",include(router.urls)),
]
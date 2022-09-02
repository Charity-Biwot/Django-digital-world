from django .urls import path
from .views import register_customer, register_receipt, register_thirdparty, register_wallet
from .views import register_currency
from .views import register_account
from .views import register_transaction
from .views import register_receipt
from .views import register_card
from .views import register_thirdparty
from .views import register_notification
from .views import register_loan
from .views import reward_register


urlpatterns = [
    path("register/", register_customer, name="registration"),
]

urlpatterns = [
    path("register/", register_currency, name="registration"),
]

urlpatterns = [
    path("register/", register_wallet, name="registration"),
]

urlpatterns = [
    path("register/", register_account, name="registration"),
]
urlpatterns=[
    path("register/", register_transaction,name="registration"),
]

urlpatterns=[
    path("register/", register_receipt,name="registration"),
]

urlpatterns=[
    path("register/", register_card,name="registration"),
]

urlpatterns=[
    path("register/", register_thirdparty,name="registration"),
]

urlpatterns=[
    path("register/", register_notification,name="registration"),
]
urlpatterns=[
    path("register/", register_loan,name="registration"),
]
urlpatterns=[
    path("register/", reward_register,name="registration"),
]
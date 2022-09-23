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

# You can use the single import statement 
# like from .views import *
# it is the best practice


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
# The best practice is to combine all 
# the link on the single list like the 
# following;
# Also try to make the link different, 
# since the link should be unique, 
# if the link are not unique django will 
# pick the first one all the time. see below

# urlpatterns = [

#     path("register/link1/", register_customer, name="registration 1"),
#     path("register/link2/", register_currency, name="registration 2"),
#     path("register/link3/", register_wallet, name="registration 3"),
#     path("register/link4/", register_account, name="registration 4"),
#     ...
# ]

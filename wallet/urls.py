from django .urls import path
from .import views
urlpatterns = [
    path("register/",views.register_customer, name="registration"),
    path("currencys/",views.register_currency, name="register_currencys"),
    path("wallets/",views.register_wallet, name="register_wallets"),
    path("accounts/",views.register_account, name="register_accounts"),
    path("transactions/",views.register_transaction,name="register_transactions"),
    path("receipts/",views.receipt_register,name="register_receipts"),
    path("card/",views.register_card,name="register_card"),
    path("thirdpartys/",views.register_third_party,name="register_thirdpartys"),
    path("notifications/",views.register_notification,name="register_notifications"),
    path("loan/", views.register_loan,name="register_loan"),
    path("rewards/",views.register_reward,name="register_rewards"),
    path("customers/",views.list_Customer,name = "register_customers"),
    path("currency/",views.list_Currency,name = "register_currency"),
    path("account/",views.list_Account,name = "register_account"),
    path("wallet/",views.list_Wallet,name = "register_wallet"),
    path("receipt/",views.list_Receipt,name = "register_receipt"),
    path("transaction/",views.list_Transaction,name = "register_transaction"),
    path("reward/",views.list_Reward,name = "register_reward"),
    path("loans/",views.list_Loan,name = "register_loans"),
    path("notification/",views.list_Notification,name = "register_notification"),
    path("cards/",views.list_Card,name = "register_cards"),
    path("thirdparty/",views.list_Thirdparty,name = "register_thirdparty"),
    path("profile/<int:id>/", views.customer_profile, name="customer_profile"),
    # path("customers/edit/<int:id>/", views.edit_customer, name="edit_customer"),
]











   


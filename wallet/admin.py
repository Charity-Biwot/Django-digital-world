from inspect import signature
from .models import Account, Currency, Customer, Notification, Receipt, Reward, Third_Party,Wallet,Transaction,Card,Loan,Reward

from django.contrib import admin
admin.site.register(Customer)
admin.site.register(Wallet)
admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Third_Party)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)

# admin.site.register(Account)
# admin.site.register(Transaction)









    

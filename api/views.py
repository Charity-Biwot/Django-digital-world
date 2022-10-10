from distutils.sysconfig import customize_compiler
# from msilib.schema import Class
from django.shortcuts import render
from rest_framework import viewsets
from wallet .models import Currency, Customer,Account, Third_party,Transaction,Loan,Receipt,Notification,Reward,Currency,Card,Third_party,Wallet
from .serializer import Customerserializer
from .serializer import Accountserializer,Transactionserializer,Loanserializer
from .serializer import Receiptserializer,Notificationserializer,Rewardserializer,Currencyserializer,Cardserializer,Thirdpartyserializer,Walletserializer

# Create your views here.
class Customerviewset (viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customerserializer
    
class Accountviewset (viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = Accountserializer
    
class Transactionviewset (viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = Transactionserializer
    
class Loanviewset (viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = Loanserializer
    
class Receiptviewset (viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = Receiptserializer

class Notificationviewset (viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = Notificationserializer
    
class Rewardviewset (viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = Rewardserializer
    
class Currencyviewset (viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = Currencyserializer

class Cardviewset (viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = Cardserializer

class Thirdpartyviewset (viewsets.ModelViewSet):
    queryset = Third_party.objects.all()
    serializer_class = Thirdpartyserializer
    
class Walletviewset (viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = Walletserializer
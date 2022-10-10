from dataclasses import field
# from pyexpat import model
from rest_framework import serializers
import wallet
from wallet .models import Customer,Account, Third_party,Transaction,Loan,Receipt,Notification,Reward,Currency,Card,Third_party,Wallet

class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        field= ("first_name","email","age")

class Accountserializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        field= ("wallet","account_type","balance","name")
        
class Transactionserializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        field= ("transaction_cost","wallet","transaction_type","origin_account","status")


class Loanserializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        field= ("loantype","amount","wallet","duedate","loanterm","interestrate","payment_date","duration","balance","guaranter")
        
class Receiptserializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        field= ("receipt_file","transaction","date")
        
class Notificationserializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        field= ("date_created","time","message","is_active","image","is_active","recipient")

class Rewardserializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        field= ("wallet","date_time_received","transaction",)
 
class Currencyserializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        field= ("currency_origin","currency_symbol","name")
        
class Cardserializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        field= ("card_number","date_issued","signature","expiry_date","card_status","security_code","issuer","account")
 
class Thirdpartyserializer(serializers.ModelSerializer):
    class Meta:
        model = Third_party
        field= ("email","phone_number","transaction_cost","currency","account","active")
 

class Walletserializer(serializers.ModelSerializer):
    class Meta:
        model = wallet
        field= ("balance","pin","currency","active")
 

 

 

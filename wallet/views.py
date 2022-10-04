import re
from django.shortcuts import redirect, render

from wallet.models import Customer,Wallet,Currency,Account,Receipt,Reward,Transaction,Loan,Notification,Card,Third_party

from .forms import CustomerRegistrationForm
from .forms import CurrencyRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import CardRegistrationForm
from .forms import Third_partyRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import RewardRegistrationForm
from .forms import AccountRegistrationForm
from .forms import WalletRegistrationForm
from .forms import LoanRegistrationForm
from .forms import NotificationRegistrationForm


# Create your views here.
def register_customer(request):
    if request.method=='POST':
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form}) 



def list_Customer(request):
    customers = Customer.objects.all()
    return render(request,"wallet/list_customers.html",{"customers":customers})
        
def register_currency(request):
  
    if request.method=="POST":
        form=CurrencyRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form":form}) 

def list_Currency(request):
        currencys=Currency.objects.all()
        return render(request,"wallet/list_currency.html",{"currencys":currencys})
        


def register_account(request):
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form}) 

def list_Account(request):
        accounts=Account.objects.all()
        return render(request,"wallet/list_account.html",{"accounts":accounts})
        
   
def register_wallet(request):
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form}) 

def list_Wallet(request):
        wallets=Wallet.objects.all()
        return render(request,"wallet/list_wallet.html",{"wallets":wallets})
        
  
def receipt_register(request):
    if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=ReceiptRegistrationForm()
    return render(request,"wallet/receipt_register.html",{"form":form}) 

def list_Receipt(request):
        receipts=Receipt.objects.all()
        return render(request,"wallet/list_receipt.html",{"receipts":receipts})
    
def register_transaction(request):
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form}) 

def list_Transaction(request):
        transactions=Transaction.objects.all()
        return render(request,"wallet/list_transaction.html",{"transactions":transactions})
        
   
def register_reward(request):
    if request.method=="POST":
        form=RewardRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=RewardRegistrationForm()
    return render(request,"wallet/reward_register.html",{"form":form}) 

def list_Reward(request):
        rewards=Reward.objects.all()
        return render(request,"wallet/list_reward.html",{"rewards":rewards})
        
   
def register_loan(request):
    if request.method=="POST":
        form=LoanRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form}) 

def list_Loan(request):
        loans=Loan.objects.all()
        return render(request,"wallet/list_loan.html",{"loans":loans})
        
   
def register_notification(request):
    if request.method=="POST":
        form=NotificationRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{"form":form}) 

def list_Notification(request):
        notifications=Notification.objects.all()
        return render(request,"wallet/list_notification.html",{"notifications":notifications})
        
    
def register_card(request):
    if request.method=="POST":
        form=CardRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form}) 

def list_Card(request):
        cards=Card.objects.all()
        return render(request,"wallet/list_card.html",{"cards":cards})
        
   

def register_third_party(request):
    if request.method=="POST":
        form=Third_partyRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
         form=Third_partyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{"form":form}) 

def list_Thirdparty(request):
        thirdPartyaccounts=Third_party.objects.all()
        return render(request,"wallet/list_thirdparty.html",{"thirdPartyaccounts":thirdPartyaccounts})
        
# def customer_profile(request, id):
#     customer=Customer.object.get(id=id)
#     return render(request,"wallet/customer_profile.html",{"customer":Customer})

# def customer_profile(request, id):
#     customer=Customer.object.get(id=id)
#     request=="POST"
    

       




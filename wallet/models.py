from django.db import models

# Create your models here.


class Currency(models.Model):
    country_origin = models.CharField(max_length=25, blank=True)
    currency_symbol = models.CharField(max_length=10, blank=True)
    currency_name = models.CharField(max_length=20, blank=True)


class Customer(models.Model):
    id_number = models.CharField(max_length=10, blank=True, primary_key=True)
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    gender_identity = (
        ('F', 'female'),
        ('M', 'male')
    )
    gender = models.CharField(
        max_length=10, choices=gender_identity, blank=False)
    address = models.TextField(max_length=15, null=True)
    age = models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(default=True)
    marital_status = models.CharField(max_length=10, blank=True)
    signature = models.ImageField(upload_to='images/', null=True)
    employment_status = models.BooleanField(default=False)


class Wallet(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        null=True,
    )
    balance = models.IntegerField()
    pin = models.PositiveSmallIntegerField()
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name='wallet_currency', null=True)
    active = models.BooleanField(null=True)
    date_created = models.DateField(null=True)
    wallet_type = models.CharField(max_length=15, null=True)
    bank_account_name = models.CharField(max_length=15, null=True)


class Account(models.Model):
    wallet = models.ForeignKey(
        'Wallet', on_delete=models.CASCADE, related_name='Account_wallet', null=True)
    name = models.CharField(max_length=15, null=True)
    account_type = models.CharField(max_length=15, null=True)
    balance = models.IntegerField()
    account_type = models.CharField(max_length=23, null=True)


class Transaction(models.Model):
    transaction_charge = models.CharField(max_length=3, null=True)
    transaction_cost = models.PositiveIntegerField(null=True)
    wallet = models.ForeignKey(
        'Wallet', on_delete=models.CASCADE, related_name='Transaction_wallet', null=True)
    transaction_type = models.CharField(max_length=15, null=True)
    origin_account = models.ForeignKey(
        'Account', on_delete=models.CASCADE, related_name='Transaction_account_origin', null=True)
    destination_account = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='Transaction_destinations', null=True)
    status = models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=15, null=True)


class Receipt(models.Model):
    receipt_file = models.FileField(upload_to='media/')
    date = models.DateField(null=True)
    transaction = models.ForeignKey(
        'Transaction', on_delete=models.CASCADE, related_name='Receipt_transaction', null=True)


class Card(models.Model):
    card_name = models.CharField(max_length=25, null=True)
    date_issued = models.DateTimeField()
    card_number = models.CharField(max_length=15, null=True)
    signature = models.ImageField(max_length=15, null=True)
    expiry_date = models.DateField()
    card_status = models.CharField(max_length=15, null=True)
    security_code = models.PositiveSmallIntegerField()
    issuer = models.CharField(max_length=35, null=True)
    account = models.ForeignKey(
        'Account', on_delete=models.CASCADE, related_name='Card_account', null=True)


class Third_party(models.Model):
    full_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15, null=True)
    transaction_cost = models.IntegerField(null=True)
    currency = models.ForeignKey(
        'Currency', on_delete=models.CASCADE, related_name='Third_party_currency', null=True)
    account = models.ForeignKey(
        'Account', on_delete=models.CASCADE, related_name='Third_party_account', null=True)
    active = models.BooleanField(null=True)


class Notification(models.Model):
    date_created = models.DateField()
    time = models.TimeField(null=True)
    message = models.CharField(max_length=40, null=True)
    is_active = models.BooleanField(null=True)
    image = models.ImageField(null=True)
    recipient = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='Notification_recipient', null=True)


class Loan(models.Model):
    interest = models.IntegerField(null=True)
    loan_type = models.CharField(max_length=15, null=True)
    amount = models.IntegerField(null=True)
    wallet = models.ForeignKey(
        'Wallet', on_delete=models.CASCADE, related_name='Loan_wallet', null=True)
    duedate = models.DateField(null=True)
    loanterm = models.CharField(max_length=35, null=True)
    interestrate = models.IntegerField(null=True)
    paymentdate = models.DateField(null=True)
    duration = models.CharField(max_length=25, null=True)
    balance = models.IntegerField()
    loanstatus = models.CharField(max_length=25, null=True)
    guaranter = models.CharField(max_length=25, null=True)


class Reward(models.Model):
    points = models.PositiveIntegerField(null=True)
    wallet = models.ForeignKey(
        'Wallet', on_delete=models.CASCADE, related_name='Reward_wallet', null=True)
    date_time_received = models.DateTimeField()
    transaction = models.ForeignKey(
        'Transaction', on_delete=models.CASCADE, related_name='Reward_transaction', null=True)

# It is best practice to track
# the date when a model is
# created or updated by adding the following;

# # Registration
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)
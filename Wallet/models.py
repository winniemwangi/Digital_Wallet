from datetime import datetime
import email
from django.db import models



# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15,null=True)
    last_name = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=16, null=True)
    Date_of_registration = models.DateTimeField(null=True) 
    phonenumber = models.CharField(max_length=10, null=True)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10, null=True)
    ID_number = models.IntegerField(null=True)


class Wallet(models.Model):
    balance = models.IntegerField(null=True)
    customer = models.ForeignKey(default=1, to=Customer, on_delete=models.CASCADE, null=True, related_name='Wallet_customer')
    Date_created = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, null=True)
    pin = models.IntegerField(null=True)
    currency = models.CharField(max_length=10, null=True)

class Account(models.Model):
    balance = models.IntegerField(null=True)
    wallet = models.ForeignKey(to=Wallet, on_delete=models.CASCADE, null=True, related_name='wallet_account')
    account_number = models.IntegerField(null=True)
    account_name = models.CharField(max_length=15, null=True)
    account_type = models.CharField(max_length=10, null=True)

class Transaction(models.Model):
    code = models.CharField(max_length=20, null=True)
    Wallet = models.ForeignKey( on_delete=models.CASCADE, to=Wallet, null=True, related_name='wallet_transaction')
    amount = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    transaction_type = models.CharField(max_length=20, null=True)
    receipt = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=True, related_name='receipt_transaction')
    transaction_charge = models.IntegerField(null=True)
    Date_time = models.DateTimeField(null=True)
    origin_Account = models.ForeignKey(on_delete=models.CASCADE, to=Account, null=True, related_name='origin_transaction')
    destination_account = models.ForeignKey( on_delete=models.CASCADE, to=Account, null=True, related_name='destination_transaction')

class Card(models.Model):
    card_number = models.IntegerField(null=True)
    card_name = models.CharField(max_length=10, null=True)
    Date_issued = models.DateTimeField(datetime.now, null=True)
    card_type = models.CharField(max_length=10, null=True)
    expiry_date = models.DateTimeField(null=True)
    security_code = models.IntegerField(null=True)
    Account = models.ForeignKey(to=Customer,on_delete=models.CASCADE, null=True, related_name='account_card')
    issuer = models.CharField(max_length=20,null=True)
    signature = models.CharField(max_length=5, null=True)

class Third_party(models.Model):
    name = models.CharField(max_length=20, null=True)
    currency = models.IntegerField(null=True)
    transaction_cost = models.IntegerField(null=True)
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, null=True, related_name='third_party_account')

class Notifications(models.Model):
    message = models.CharField(null=True, max_length=10)
    title = models.CharField(null=True, max_length=10)
    recepient = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=True, related_name='recepient_notification')
    status = models.CharField(null=True, max_length=10)
    date_time = models.DateTimeField(null=True)

class Receipt(models.Model):
    receipt_type = models.CharField(null=True, max_length=10)
    date = models.DateTimeField(null=True)
    transaction = models.ForeignKey(null=True, to=Transaction, on_delete=models.CASCADE, related_name='receipt_transaction')
    file = models.FileField(null=True)

class Loan(models.Model):
    loan_id = models.IntegerField(null=True)
    purpose = models.CharField(null=True, max_length=10)
    amount = models.IntegerField(null=True)
    loan_status = models.CharField(null=True, max_length=10)
    date_issued = models.DateTimeField(null=True)
    wallet = models.ForeignKey(null=True, to=Wallet, on_delete=models.CASCADE, related_name='loan_wallet')
    interest_rate = models.IntegerField(null=True)
    payment_due_date = models.DateTimeField(null=True)
    loan_balance = models.IntegerField(null=True)
    guarantor = models.ForeignKey(null=True, to=Customer, on_delete=models.CASCADE, related_name='loan_guarantor')

class Rewards(models.Model):
    recepient = models.ForeignKey(null=True, to=Wallet, on_delete=models.CASCADE, related_name='recepient_rewards')
    date_of_reward = models.DateTimeField(null=True)
    wallet = models.ForeignKey(null=True, to=Wallet, on_delete=models.CASCADE, related_name='walllet_reward')
    points = models.BigIntegerField(null=True)

class Currency(models.Model):
    country_of_origin = models.CharField(null=True, max_length=10)
    symbol = models.CharField(null=True, max_length=10)
    Amount = models.BigIntegerField(null=True)


    


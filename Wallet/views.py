from django.shortcuts import render

# from Wallet.models import Customer
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptRegistrationForm, RewardsRegistrationForm, ThirdpartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
# Handles http request

def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"Wallet/register_customer.html",{"form":form})

def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request,"Wallet/wallet_customer.html",{"form":form})

def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"Wallet/account_customer.html",{"form":form})

def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request,"Wallet/account_customer.html",{"form":form})

def register_card(request):
    form = CardRegistrationForm()
    return render(request,"Wallet/card_customer.html",{"form":form})

def register_thirdparty(request):
    form = ThirdpartyRegistrationForm()
    return render(request,"Wallet/thirdparty_customer.html",{"form":form})

def register_notification(request):
    form = NotificationsRegistrationForm()
    return render(request,"Wallet/thirdparty_customer.html",{"form":form})

def register_receipt(request):
    form = ReceiptRegistrationForm()
    return render(request,"Wallet/receipt.html",{"form":form})

def register_loan(request):
    form = LoanRegistrationForm()
    return render(request,"Wallet/loan_customer.html",{"form":form})

def register_rewards(request):
    form = RewardsRegistrationForm()
    return render(request,"Wallet/rewards_customer.html",{"form":form})

def register_currency(request):
    form = CurrencyRegistrationForm()
    return render(request,"Wallet/currency_customer.html",{"form":form})



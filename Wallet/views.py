from django.shortcuts import render

from Wallet.models import Account, Customer, Wallet

# from Wallet.models import Customer
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptRegistrationForm, RewardsRegistrationForm, ThirdpartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
# Handles http request

def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CustomerRegistrationForm()
    return render(request,"Wallet/register_customer.html",{"form":form})

def list_customer(request):
    customer = Customer.objects.all()
    return render(request,"Wallet/customer_list.html",{"customer":customer})

def register_account(request):
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
        return render(request,"wallet/account.html",{"form":form})
def list_account(request):
    accounts=Account.objects.all()
    return render(request,"wallet/account_list.html",{"accounts":accounts})


def register_wallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = WalletRegistrationForm()
    return render(request,"wallet.html",{"form":form})

def list_wallets(request):
    wallet = Wallet.objects.all()
    return render(request,"wallet/wallets_list.html",{"wallet":wallet})





def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request,"Wallet/account_customer.html",{"form":form})

def register_card(request):
    form = CardRegistrationForm()
    return render(request,"Wallet/card_customer.html",{"form":form})

def register_thirdparty(request):
    if request.method == "POST":
        form = ThirdpartyRegistrationForm(request.Post)
        if form.is_valid():
            form.save()

    else:
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



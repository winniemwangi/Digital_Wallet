# from tkinter.tix import Form
from django.shortcuts import render,redirect

from Wallet.models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Rewards, Third_party, Transaction, Wallet

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
    return render(request,"wallet/register_customer.html",{"form":form})

def list_customer(request):
    customers = Customer.objects.all()
    return render(request,"wallet/customer_list.html",{"customers":customers})




def register_account(request):
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
        return render(request,"wallet/account_customer.html",{"form":form})
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
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
           form.save()

    else:
        form = TransactionRegistrationForm()
    return render(request,"wallet/account_customer.html",{"form":form})

def list_transaction(request):
    transaction = Transaction.objects.all()
    return render(request,"wallet/transaction_list.html",{"transaction":transaction})



def register_card(request):
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
           form.save()

    else:
        form = CardRegistrationForm()
    return render(request,"wallet/card_customer.html",{"form":form})

def list_card(request):
    card = Card.objects.all()
    return render(request,"wallet/card_list.html",{"card":card})




def register_thirdparty(request):
    if request.method == "POST":
        form = ThirdpartyRegistrationForm(request.Post)
        if form.is_valid():
            form.save()

    else:
        form = ThirdpartyRegistrationForm()

    return render(request,"wallet/thirdparty_customer.html",{"form":form})
    
def list_thirdparty(request):
    thirdparty = Third_party.objects.all()
    return render(request,"wallet/thirdparty_list.html",{"thirdparty":thirdparty})


def register_notification(request):
    if request.method == "POST":
        form = NotificationsRegistrationForm(request.Post)
        if form.is_valid():
            form.save()

    else:
        form = NotificationsRegistrationForm()

    return render(request,"wallet/notifications_customer.html",{"form":form})

def list_notification(request):
    notification = Notifications.objects.all()
    return render(request,"wallet/notification_list.html",{"notification":notification})

def register_receipt(request):
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.Post)
        if form.is_valid():
            form.save()

    else:
        form = ReceiptRegistrationForm()

    return render(request,"wallet/receipt.html",{"form":form})

def list_receipt(request):
    receipt = Receipt.objects.all()
    return render(request,"wallet/receipt_list.html",{"receipt":receipt})



def register_loan(request):
    if request.method == "POST":
        form = LoanRegistrationForm(request.Post)
        if form.is_valid():
            form.save()

    else:
        form = LoanRegistrationForm()

    return render(request,"wallet/loan_customer.html",{"form":form})

def list_loan(request):
    loan = Loan.objects.all()
    return render(request,"wallet/loan_list.html",{"loan":loan})

def register_rewards(request):
    if request.method == "POST":
        form = RewardsRegistrationForm(request.Post)
        if form.is_valid():
            form.save()

    else:
        form = RewardsRegistrationForm()

    return render(request,"wallet/rewards_customer.html",{"form":form})

def list_rewards(request):
    reward = Rewards.objects.all()
    return render(request,"wallet/reward_list.html",{"reward":reward})


def register_currency(request):
    if request.method == "POST":
        form = CurrencyRegistrationForm(request.Post)
        if form.is_valid():
            form.save()

    else:
        form = CurrencyRegistrationForm()
    
    return render(request,"wallet/currency_customer.html",{"form":form})

def list_currency(request):
    currency = Currency.objects.all()
    return render(request,"wallet/currency_list.html",{"currency":currency})


def customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "wallet/customer_profile.html", {"customer": customer})


def edit_profile(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id = customer.id)

       
    else:
            form = CustomerRegistrationForm(instance=customer)
            return render(request, "wallet/edit_profile.html", {"form": form})


def wallet_profile(request, id):
    wallet = Wallet.objects.get(id=id)
    return render(request, "wallet/wallet_profile.html", {"wallet": wallet})


def edit_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_profile", id = wallet.id)

       
    else:
            form = WalletRegistrationForm(instance=wallet)
            return render(request, "wallet/edit_profile.html", {"form": form})
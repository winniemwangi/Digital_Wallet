from django.contrib import admin

# Register your models here.
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Rewards, Third_party, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
    list_display =("first_name","last_name","address",)
    search_fields = ("first_name", "last_name",)
admin.site.register(Customer, CustomerAdmin) 

class WalletAdmin(admin.ModelAdmin):
    list_display = ("balance","customer","status")
    search_fields = ('balance','customer')
admin.site.register(Wallet)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('balance','account_name', 'account_number')
    search_fields = ('account_name', 'account_name')
admin.site.register(Account)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount','number','code')
    search_fields = ('amount','number')
admin.site.register(Transaction)

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'card_type', 'card_name')
    search_fields = ('card_type', 'card_name')
admin.site.register(Card)

class Third_PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'transaction_cost')
    search_fields = ('name', 'account')
admin.site.register(Third_party)

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'recepient')
    search_fields = ('title', 'recepient')
admin.site.register(Notifications)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'date', 'file')
    search_fields = ('date', 'transaction')
admin.site.register(Receipt)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'amount', 'balance')
    search_fields = ('loan_id', 'amount')
admin.site.register(Loan)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('recepient', 'wallet', 'points')
    search_fields = ('wallet', 'points')
admin.site.register(Rewards)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'country_of_origin', 'Amount')
    search_fields = ('symbol', 'Amount')
admin.site.register(Currency)
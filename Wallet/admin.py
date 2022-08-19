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
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name','account_number', 'balance')
    search_fields = ('account_name', 'account_name')
admin.site.register(Account, AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('number','code','amount')
    search_fields = ('amount','number')
admin.site.register(Transaction, TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'card_number', 'card_type')
    search_fields = ('card_type', 'card_name')
admin.site.register(Card, CardAdmin)

class Third_PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'transaction_cost')
    search_fields = ('name', 'account')
admin.site.register(Third_party, Third_PartyAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'recepient')
    search_fields = ('title', 'recepient')
admin.site.register(Notifications, NotificationsAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'date', 'file')
    search_fields = ('date', 'transaction')
admin.site.register(Receipt, ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'amount', 'loan_balance')
    search_fields = ('loan_id', 'amount')
admin.site.register(Loan, LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('recepient', 'wallet', 'points')
    search_fields = ('wallet', 'points')
admin.site.register(Rewards, RewardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'country_of_origin', 'amount')
    search_fields = ('symbol', 'amount')
admin.site.register(Currency, CurrencyAdmin)
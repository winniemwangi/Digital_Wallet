from django.contrib import admin

# Register your models here.
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Rewards, Third_party, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
    list_display =("first_name","last_name","address",)
    search_fields = ("first_name", "last_name",)


admin.site.register(Customer, CustomerAdmin) 
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Third_party)
admin.site.register(Notifications)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Rewards)
admin.site.register(Currency)
from rest_framework import serializers
from Wallet.models import Account, Card, Customer, Loan, Notifications, Receipt, Transaction, Wallet


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "email", "age")

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("customer", "balance", "status")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_name", "account_number", "balance")

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("card_name", "card_number", "card_type")

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("wallet", "number", "transaction_type")

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("loan_id", "wallet", "loan_status")

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("receipt_type", "date", "transaction")

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ("title", "message", "recepient")
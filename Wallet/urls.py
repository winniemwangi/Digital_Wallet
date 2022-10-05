from django.urls import path
from .views import account_profile, card_profile, customer_profile, edit_profile, list_account, list_card, list_currency, list_loan, list_notification, list_receipt, list_rewards, list_thirdparty, list_transaction, list_wallets, receipt_profile, register_account, list_customer, register_card, register_currency, register_customer, register_loan, register_notification, register_receipt, register_rewards, register_thirdparty, register_transaction, register_wallet, transaction_profile, wallet_profile

urlpatterns = [
    path("register/", register_customer, name="registration"),
    path("wallet/", register_wallet, name="registration"),
    path("account/", register_account, name="registration"),
    path("transaction/", register_transaction, name="registration"),
    path("card/", register_card, name="registration"),
    path("thirdparty/", register_thirdparty, name="registration"),
    path("notifications/", register_notification, name="registration"),
    path("receipt/", register_receipt, name="registration"),
    path("loan/", register_loan, name="registration"),
    path("rewards/", register_rewards, name="registration"),
    path("currency/", register_currency, name="registration"),
    path("customers/", list_customer, name="customers_list"),
    path("wallets/",list_wallets,name="wallets_list"),
    path("accounts/", list_account, name="account_list"),
    path("transactions/", list_transaction, name="transaction_list"),
    path("cards/", list_card, name="card_list"),
    path("thirdpartys/", list_thirdparty, name="thirdparty_list"),
    path("notification/", list_notification, name="notification_list"),
    path("receipts/", list_receipt, name="receipt_list"),
    path("loans/", list_loan, name="loan_list"),
    path("reward/", list_rewards, name="reward_list"),
    path("currencys/", list_currency, name="currency_list"),
    path("customer/<int:id>/", customer_profile, name="customer_profile"),
    path("customer/edit/<int:id>/", edit_profile, name="edit_profile"),
    path("wallet/<int:id>/", wallet_profile, name="wallet_profile"),
    path("wallet/edit/<int:id>/", edit_profile, name="edit_profile"),
    path("Accounts/<int:id>/", account_profile, name="account_profile"),
    path("Accounts/edit/<int:id>/", edit_profile, name="edit_profile"),
    path("Card/<int:id>/", card_profile, name="card_profile"),
    path("Card/edit/<int:id>/", edit_profile, name="edit_profile"),
    path("Transaction/<int:id>/", transaction_profile, name="transaction_profile"),
    path("Transaction/edit/<int:id>/", edit_profile, name="edit_profile"),
    path("Receipt/<int:id>/", receipt_profile, name="receipt_profile"),
    path("Receipt/edit/<int:id>/", edit_profile, name="edit_profile"),
    ]



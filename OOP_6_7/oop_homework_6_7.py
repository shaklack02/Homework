# Python - OOP - Multiple Inheritance & Interfaces

from abc import ABC, abstractmethod
from enum import Enum


class BankNames(Enum):
    Hapoalim = "Bank Hapoalim"
    Leomi = "Bank Leomi"
    Discount = "Bank Discount"


class CompnayCuatomer:
    def __init__(self, company_customer_id: int, name: str, bank_name: BankNames, amount_of_money: int):
        self._companyCustomer_id = company_customer_id
        self._companyCustomer_name = name
        self._companyCustomer_Bank_name = bank_name
        self._companyCustomer_amount_of_money = amount_of_money


class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, bank_name: BankNames, credit_card_number: int, amount_of_money: int):
        self._customer_id = customer_id
        self._customer_first_name = first_name
        self._customer_last_name = last_name
        self._customer_Bank_name = bank_name
        self._customer_credit_card_number = credit_card_number
        self._customer_amount_of_money = amount_of_money


class Bank:
    def __init__(self, bank_id: int, name: BankNames, amount_of_employees: int, revenue: int, expenses: int, bank_customers: []):
        self._bank_id = bank_id
        self._bank_name = name
        self._bank_number_of_employees = amount_of_employees
        self._bank_amount_of_revenue = revenue
        self._bank_amount_of_expenses = expenses
        self._bank_customers = bank_customers  # must have at lest 3 costomers

    def take_payment(self, customer: Customer, payment: int):
        # take payment from existing customer
        # (you should check if this customer is really a customer of the bank first)
        pass

    def increase_revenue(self, revenue_to_add: int):
        # - increase the bank revenue by the amount passed as reveneue_to_add
        pass

    def increase_expenses(self, expenses_to_increase: int):
        # -  increase the bank expenses by the amount passed as expensesToAdd
        pass

    def calculate_customer_money(self):
        # which should update the bank revenue according to the result of this calculation
        # However, each specific bank handle the revenue calculation
        # differently:
        pass

if __name__ == '__main__':
    # main thread
    pass
    # Bank_Hapoalim =
    # Bank_Leomi =
    # Bank_Discount =




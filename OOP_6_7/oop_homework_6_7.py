# Python - OOP - Multiple Inheritance & Interfaces

from abc import ABC, abstractmethod
from enum import Enum


class BankNames(Enum):
    Hapoalim = "Bank Hapoalim"
    Leomi = "Bank Leomi"
    Discount = "Bank Discount"


class CompanyCustomer:
    def __init__(self, company_customer_id: int, name: str, bank_name: BankNames, company_amount_of_money: int):
        self._companyCustomer_id = company_customer_id
        self._companyCustomer_name = name
        self._companyCustomer_Bank_name = bank_name
        self._companyCustomer_amount_of_money = company_amount_of_money

    @property
    def company_customer_amount_of_money(self):
        return self._companyCustomer_amount_of_money

    # Customers should also have a get_payment(salary: int)
    # method that should indicate that the customer got his monthly payment
    # and your system should increase his amount of money accordingly.
    def get_payment(self, salary: int):
        self._companyCustomer_amount_of_money += salary


class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, bank_name: BankNames, credit_card_number: int,
                 amount_of_money: int):
        self._customer_id = customer_id
        self._customer_first_name = first_name
        self._customer_last_name = last_name
        self._customer_Bank_name = bank_name
        self._customer_credit_card_number = credit_card_number
        self._customer_amount_of_money = amount_of_money

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def bank_name(self):
        return self._customer_Bank_name

    @property
    def customer_amount_of_money(self):
        return self._customer_amount_of_money

    @customer_amount_of_money.setter
    def customer_amount_of_money(self, amount):
        self._customer_amount_of_money = amount

    # Customers should also have a get_payment(salary: int)
    # method that should indicate that the customer got his monthly payment
    # and your system should increase his amount of money accordingly.
    def get_payment(self, salary: int):
        self._customer_amount_of_money += salary


class Bank:
    def __init__(self, bank_id: int, name: BankNames, amount_of_employees: int, revenue: int, expenses: int,
                 bank_customers: []):
        self._bank_id = bank_id
        self._bank_name = name
        self._bank_number_of_employees = amount_of_employees
        self._bank_amount_of_revenue = revenue
        self._bank_amount_of_expenses = expenses
        self._bank_customers = bank_customers  # must have at lest 3 costomers


    # Done
    def take_payment(self, customer: Customer, payment: int):
        # take payment from existing customer
        # (you should check if this customer is really a customer of the bank first)
        # Each time a bank handles customer payment the customer amount of money should decrease accordingly.
        if customer.customer_id in self._bank_customers and self._bank_name == customer.bank_name:
            self._bank_amount_of_revenue += payment
            customer.customer_amount_of_money -= payment
        else:
            print("Sorry you are not member of that Bank")

    def increase_revenue(self, revenue_to_add: int):
        # - increase the bank revenue by the amount passed as reveneue_to_add
        self._bank_amount_of_revenue += revenue_to_add

    def increase_expenses(self, expenses_to_increase: int):
        # -  increase the bank expenses by the amount passed as expensesToAdd
        self._bank_amount_of_expenses += expenses_to_increase

    # Done
    def calculate_customer_money(self):
        # which should update the bank revenue according to the result of this calculation
        # However, each specific bank handle the revenue calculation
        # differently:
        customers_money_sum = 0
        match self._bank_name:
            case self._bank_name.Hapoalim | self._bank_name.Discount:
                for money in self._bank_customers:
                    if isinstance(money, Customer):
                        customers_money_sum += money.customer_amount_of_money
                    else:
                        customers_money_sum += money.company_customer_amount_of_money
                self.increase_expenses(customers_money_sum)
            case self._bank_name.Leomi:
                for money in self._bank_customers:
                    customers_money_sum += money.customer_amount_of_money
                self.increase_expenses(self._bank_amount_of_revenue - customers_money_sum)
            case _:
                print("Error: This account is with an unrecognized bank.")


if __name__ == '__main__':
    # main thread
    pass
    # Bank_Hapoalim =
    # Bank_Leomi =
    # Bank_Discount =




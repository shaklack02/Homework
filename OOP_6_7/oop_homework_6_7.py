# Python - OOP - Multiple Inheritance & Interfaces

from abc import ABC, abstractmethod

class Bank:
    def __init__(self, id, name, number_of_emplyees, amount_of_revenue, amount_of_expenses, bank_customers):
        self._bank_id = id
        self._bank_name = name
        self._bank_number_of_employees = number_of_emplyees
        self._bank_amounr_of_revenue = amount_of_revenue
        self._bank_amount_of_expenses = amount_of_expenses
        self._bank_costomers = bank_customers # must have at lest 3 costomers

class Customer:
    def __init__(self):
        pass


    def take_payment(customer: Customer, payment: int):
        # take payment from existing customer
        # (you should check if this customer is really a customer of the bank first)
        pass

    def increase_revenue(reveneue_to_add: int):
        # - increase the bank revenue by the amount passed as reveneue_to_add
        pass

    def increase_expenses(expenses_to_increase: int):
        # -  increase the bank expenses by the amount passed as expensesToAdd
        pass

    def calculate_customer_money():
        # which should update the bank revenue according to the result of this calculation
        # However, each specific bank handle the revenue calculation
        # differently:
        pass




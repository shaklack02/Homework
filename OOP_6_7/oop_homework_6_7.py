from abc import ABC, abstractmethod
from enum import Enum


class BankName(Enum):
    Hapoalim = "Bank Hapoalim"
    Leomi = "Bank Leomi"
    Discount = "Bank Discount"


class CustomerPays(ABC):
    @abstractmethod
    def receive_payment(self, amount: int):
        pass

    @abstractmethod
    def deduct_payment(self, amount: int):
        pass


class Customer(CustomerPays):
    def __init__(self, customer_id: int, first_name: str, last_name: str, bank_name: BankName,
                 credit_card_number: int, amount_of_money: int):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._bank_name = bank_name
        self._credit_card_number = credit_card_number
        self._amount_of_money = amount_of_money

    @property
    def bank_name(self):
        return self._bank_name

    @property
    def amount_of_money(self):
        return self._amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, amount):
        if isinstance(amount, int) and amount >= 0:
            self._amount_of_money = amount
        else:
            raise ValueError("Error: value must be a non-negative integer.")

    def receive_payment(self, amount: int):
        if amount >= 0:
            self._amount_of_money += amount
        else:
            raise ValueError("Error: Payment must be a positive integer.")

    def deduct_payment(self, amount: int):
        if amount >= 0 and self._amount_of_money >= amount:
            self._amount_of_money -= amount
        else:
            raise ValueError("Error: Insufficient funds or invalid amount.")


class CompanyCustomer(CustomerPays):
    def __init__(self, company_customer_id: int, name: str, bank_name: BankName, amount_of_money: int):
        self._company_customer_id = company_customer_id
        self._name = name
        self._bank_name = bank_name
        self._amount_of_money = amount_of_money

    @property
    def name(self):
        return self._name

    @property
    def amount_of_money(self):
        return self._amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, amount):
        if isinstance(amount, int) and amount >= 0:
            self._amount_of_money = amount
        else:
            raise ValueError("Error: value must be a non-negative integer.")

    def receive_payment(self, amount: int):
        if amount >= 0:
            self._amount_of_money += amount
        else:
            raise ValueError("Error: Payment must be a positive integer.")

    def deduct_payment(self, amount: int):
        if amount >= 0 and self._amount_of_money >= amount:
            self._amount_of_money -= amount
        else:
            raise ValueError("Error: Insufficient funds or invalid amount.")


class Bank(ABC):
    def __init__(self, bank_id: int, name: BankName, amount_of_employees: int, revenue: int, expenses: int,
                 bank_customers: list):
        self._bank_id = bank_id
        self._bank_name = name
        self._bank_number_of_employees = amount_of_employees
        self._bank_amount_of_revenue = revenue
        self._bank_amount_of_expenses = expenses
        self._bank_customers = []

        if self._bank_name != BankName.Discount:
            self._bank_customers = [customer for customer in bank_customers if isinstance(customer, Customer)]
        else:
            self._bank_customers = bank_customers.copy()

    def take_payment(self, customer: CustomerPays, payment: int):
        if isinstance(payment, int) and payment >= 0:
            if customer in self._bank_customers:
                customer.deduct_payment(payment)
                self._bank_amount_of_revenue += payment
            else:
                print(f"Sorry, {customer} is not a member of {self._bank_name.value}")
        else:
            raise ValueError("Error: Payment must be a non-negative integer.")

    def increase_revenue(self, revenue_to_add: int):
        if isinstance(revenue_to_add, int) and revenue_to_add >= 0:
            self._bank_amount_of_revenue += revenue_to_add
        else:
            raise ValueError("Error: Revenue must be a non-negative integer.")

    def increase_expenses(self, expenses_to_increase: int):
        if isinstance(expenses_to_increase, int) and expenses_to_increase >= 0:
            self._bank_amount_of_expenses += expenses_to_increase
        else:
            raise ValueError("Error: Expenses must be a non-negative integer.")

    @abstractmethod
    def calculate_customer_money(self):
        pass


class BankHapoalim(Bank):
    def calculate_customer_money(self):
        total_money = sum(
            customer.amount_of_money for customer in self._bank_customers if isinstance(customer, Customer))
        self._bank_amount_of_revenue += total_money


class BankLeomi(Bank):
    def calculate_customer_money(self):
        total_money = sum(
            customer.amount_of_money for customer in self._bank_customers if isinstance(customer, Customer))
        self._bank_amount_of_revenue -= total_money


class BankDiscount(Bank):
    def calculate_customer_money(self):
        total_money = sum(customer.amount_of_money for customer in self._bank_customers)
        self._bank_amount_of_revenue = total_money


if __name__ == '__main__':
    # Test Data
    customer_1 = Customer(101, "Alice", "Smith", BankName.Hapoalim, 1234567890123456, 15000)
    company_customer_1 = CompanyCustomer(401, "Tech Innovations Ltd.", BankName.Discount, 150000)
    discount_members = [company_customer_1, customer_1]

    bank_hapoalim = BankHapoalim(101, BankName.Hapoalim, 100, 500000, 200000, [customer_1])
    bank_discount = BankDiscount(103, BankName.Discount, 150, 700000, 300000, discount_members)

    # Take payments
    bank_hapoalim.take_payment(customer_1, 500)
    bank_discount.take_payment(company_customer_1, 2000)

    # Calculate customer money
    bank_hapoalim.calculate_customer_money()
    bank_discount.calculate_customer_money()

    # Output the bank revenue
    print(f"Bank Hapoalim revenue: {bank_hapoalim._bank_amount_of_revenue}")
    print(f"Bank Discount revenue: {bank_discount._bank_amount_of_revenue}")

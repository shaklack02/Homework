from abc import ABC, abstractmethod
from enum import Enum


class BankNames(Enum):
    Hapoalim = "Bank Hapoalim"
    Leomi = "Bank Leomi"
    Discount = "Bank Discount"


class CompanyCustomer:
    def __init__(self, company_customer_id: int, name: str, bank_name: BankNames, company_amount_of_money: int):
        self._company_customer_id = company_customer_id
        self._company_customer_name = name
        self._company_customer_bank_name = bank_name
        self._company_customer_amount_of_money = company_amount_of_money

    @property
    def company_customer_name(self):
        return self._company_customer_name

    @property
    def company_customer_amount_of_money(self):
        return self._company_customer_amount_of_money

    @company_customer_amount_of_money.setter
    def company_customer_amount_of_money(self, amount):
        self._company_customer_amount_of_money = amount


    def get_payment(self, salary: int):
        # Add salary to company amount of money
        self._company_customer_amount_of_money += salary


class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, bank_name: BankNames, credit_card_number: int,
                 amount_of_money: int):
        self._customer_id = customer_id
        self._customer_first_name = first_name
        self._customer_last_name = last_name
        self._customer_bank_name = bank_name
        self._customer_credit_card_number = credit_card_number
        self._customer_amount_of_money = amount_of_money


    @property
    def customer_bank_name(self):
        return self._customer_bank_name

    @property
    def customer_amount_of_money(self):
        return self._customer_amount_of_money

    @customer_amount_of_money.setter
    def customer_amount_of_money(self, amount):
        self._customer_amount_of_money = amount

    def get_payment(self, salary: int):
        # Add salary to customer amount of money
        self._customer_amount_of_money += salary


class Bank(ABC):
    def __init__(self, bank_id: int, name: BankNames, amount_of_employees: int, revenue: int, expenses: int,
                 bank_customers: list):
        self._bank_id = bank_id
        self._bank_name = name
        self._bank_number_of_employees = amount_of_employees
        self._bank_amount_of_revenue = revenue
        self._bank_amount_of_expenses = expenses
        self._bank_customers = bank_customers  # At least 3 customers

    def take_payment(self, customer, payment: int):
        # Check if customer belongs to the bank
        if isinstance(customer, CompanyCustomer):
            if customer not in self._bank_customers or self._bank_name != customer.company_customer_name:
                print(f"Sorry, {customer.company_customer_name} is not a member of this bank.")
                return
        else:
            if customer not in self._bank_customers or self._bank_name != customer.customer_bank_name:
                print(f"Sorry, {customer.customer_bank_name} is not a member of this bank.")
                return

        if isinstance(customer, Customer):
            self._bank_amount_of_revenue += payment
            customer.customer_amount_of_money -= payment
        elif isinstance(customer, CompanyCustomer) and self._bank_name == BankNames.Discount:
            self._bank_amount_of_revenue += payment
            customer.company_customer_amount_of_money -= payment
        else:
            print(f"{self._bank_name.value} cannot handle CompanyCustomer payments.")

    def increase_revenue(self, revenue_to_add: int):
        self._bank_amount_of_revenue += revenue_to_add

    def increase_expenses(self, expenses_to_increase: int):
        self._bank_amount_of_expenses += expenses_to_increase

    @abstractmethod
    def calculate_customer_money(self):
        pass


class BankHapoalim(Bank):
    # IF subclass init not defined than automatically the parent init will be called
    def calculate_customer_money(self):
        customers_money_sum = 0
        for customer in self._bank_customers:
            if isinstance(customer, Customer):
                customers_money_sum += customer.customer_amount_of_money
            else:
                raise TypeError(f"{self._bank_name.value} cannot manage CompanyCustomer.")
        self._bank_amount_of_revenue += customers_money_sum


class BankLeomi(Bank):
    def calculate_customer_money(self):
        customers_money_sum = 0
        for customer in self._bank_customers:
            if isinstance(customer, Customer):
                customers_money_sum += customer.customer_amount_of_money
            else:
                raise TypeError(f"{self._bank_name.value} cannot manage CompanyCustomer.")
        self._bank_amount_of_revenue -= customers_money_sum


class BankDiscount(Bank):
    def calculate_customer_money(self):
        customers_money_sum = 0
        for customer in self._bank_customers:
            if isinstance(customer, Customer):
                customers_money_sum += customer.customer_amount_of_money
            elif isinstance(customer, CompanyCustomer):
                customers_money_sum += customer.company_customer_amount_of_money
            else:
                TypeError(f"Unsupported customer")
        self._bank_amount_of_revenue = customers_money_sum


if __name__ == '__main__':
    # Create customers for testing
    customer_1 = Customer(1, "John", "Doe", BankNames.Hapoalim, 1234567890, 5000)
    customer_2 = Customer(2, "Jane", "Doe", BankNames.Leomi, 9876543210, 7000)
    customer_3 = Customer(3, "Alice", "Smith", BankNames.Discount, 1111222233, 10000)

    # Create a company customer
    company_customer_1 = CompanyCustomer(1, "TechCorp", BankNames.Discount, 15000)

    # Initialize Banks with customers
    bank_hapoalim = BankHapoalim(101, BankNames.Hapoalim, 100, 500000, 200000, [customer_1])
    bank_leomi = BankLeomi(102, BankNames.Leomi, 120, 600000, 250000, [customer_2])
    bank_discount = BankDiscount(103, BankNames.Discount, 150, 700000, 300000, [customer_3, company_customer_1])

    # Take payments
    bank_hapoalim.take_payment(customer_1, 500)
    bank_leomi.take_payment(customer_2, 700)
    bank_discount.take_payment(customer_3, 1000)
    bank_discount.take_payment(company_customer_1, 2000)

    # Calculate customer money for each bank
    bank_hapoalim.calculate_customer_money()
    bank_leomi.calculate_customer_money()
    bank_discount.calculate_customer_money()

    # Output the bank revenue
    print(f"Bank Hapoalim revenue: {bank_hapoalim._bank_amount_of_revenue}")
    print(f"Bank Leomi revenue: {bank_leomi._bank_amount_of_revenue}")
    print(f"Bank Discount revenue: {bank_discount._bank_amount_of_revenue}")

from abc import ABC, abstractmethod
from enum import Enum


class BankName(Enum):
    Hapoalim = "Bank Hapoalim"
    Leomi = "Bank Leomi"
    Discount = "Bank Discount"


class CustomerPays(ABC):
    class CustomerPays:
        def get_payment(self, salary: int):
            try:
                if isinstance(salary, int) and salary >= 0:
                    if isinstance(self, Customer):
                        self._customer_amount_of_money += salary
                    elif isinstance(self, CompanyCustomer):
                        self._company_customer_amount_of_money += salary
                else:
                    raise ValueError("Error: value must be a non-negative integer.")
            except ValueError as e:
                print(e)


class CompanyCustomer(CustomerPays):
    def __init__(self, company_customer_id: int, name: str, bank_name: BankName, company_amount_of_money: int):
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


class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, bank_name: BankName, credit_card_number: int,
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
        # Add salary to customer amount of money
        try:
            if isinstance(amount, int) and amount >= 0:
                self._customer_amount_of_money = amount
            else:
                raise ValueError("Error: value must be a non-negative integer.")
        except ValueError as e:
            print(e)


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
            for customer in bank_customers:
                if isinstance(customer, Customer):
                    self._bank_customers.append(customer)
                else:
                    print(f"Sorry {customer} is not a member of {self._bank_name.value}")
        else:
            self._bank_customers = bank_customers.copy()

    def take_payment(self, customer, payment: int):
        try:
            if isinstance(payment, int) and payment >= 0:
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
                elif isinstance(customer, CompanyCustomer) and self._bank_name == BankName.Discount:
                    self._bank_amount_of_revenue += payment
                    customer.company_customer_amount_of_money -= payment
                else:
                    print(f"{self._bank_name.value} cannot handle CompanyCustomer payments.")
            else:
                raise ValueError("Error: value must be a non-negative integer.")

        except ValueError as e:
            print(e)

    def increase_revenue(self, revenue_to_add: int):
        try:
            if isinstance(revenue_to_add, int) and revenue_to_add >= 0:
                self._bank_amount_of_revenue += revenue_to_add
            else:
                raise ValueError("Error: value must be a non-negative integer.")
        except ValueError as e:
            print(e)

    def increase_expenses(self, expenses_to_increase: int):
        try:
            if isinstance(expenses_to_increase, int) and expenses_to_increase >= 0:
                self._bank_amount_of_expenses += expenses_to_increase
            else:
                raise ValueError("Error: value must be a non-negative integer.")
        except ValueError as e:
            print(e)

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
    # Customers for Bank Hapoalim
    customer_1 = Customer(101, "Alice", "Smith", BankName.Hapoalim, 1234567890123456, 15000)
    customer_2 = Customer(102, "Bob", "Johnson", BankName.Hapoalim, 2345678901234567, 20000)
    customer_3 = Customer(103, "Charlie", "Williams", BankName.Hapoalim, 3456789012345678, 25000)

    # Customers for Bank Leomi
    customer_4 = Customer(201, "David", "Brown", BankName.Leomi, 4567890123456789, 30000)
    customer_5 = Customer(202, "Eva", "Jones", BankName.Leomi, 5678901234567890, 35000)
    customer_6 = Customer(203, "Frank", "Garcia", BankName.Leomi, 6789012345678901, 40000)

    # Customers for Bank Discount (individual customers)
    customer_7 = Customer(301, "Grace", "Miller", BankName.Discount, 7890123456789012, 50000)
    customer_8 = Customer(302, "Hannah", "Davis", BankName.Discount, 8901234567890123, 55000)
    customer_9 = Customer(303, "Isaac", "Rodriguez", BankName.Discount, 9012345678901234, 60000)

    # Company Customers for Bank Discount
    company_customer_1 = CompanyCustomer(401, "Tech Innovations Ltd.", BankName.Discount, 150000)
    company_customer_2 = CompanyCustomer(402, "Green Energy Corp.", BankName.Discount, 250000)
    company_customer_3 = CompanyCustomer(403, "Foodies Delight Inc.", BankName.Discount, 300000)
    discount_members = [company_customer_1, company_customer_2, company_customer_3, customer_7, customer_8, customer_9]

    # Initialize Banks with customers
    bank_hapoalim = BankHapoalim(101, BankName.Hapoalim, 100, 500000, 200000, [customer_1,customer_2, customer_3])
    bank_leomi = BankLeomi(102, BankName.Leomi, 120, 600000, 250000, [customer_4, customer_5, customer_6])
    bank_discount = BankDiscount(103, BankName.Discount, 150, 700000, 300000, discount_members)

    # Take payments
    bank_hapoalim.take_payment(customer_1, 500)
    bank_leomi.take_payment(customer_2, 700)
    bank_discount.take_payment(customer_3, 1000)
    bank_discount.take_payment(company_customer_1, 2000)
    bank_leomi.take_payment(company_customer_1, 700)
    bank_leomi.take_payment(customer_3, 700)

    # Calculate customer money for each bank
    bank_hapoalim.calculate_customer_money()
    bank_leomi.calculate_customer_money()
    bank_discount.calculate_customer_money()

    # Output the bank revenue
    print(f"Bank Hapoalim revenue: {bank_hapoalim._bank_amount_of_revenue}")
    print(f"Bank Leomi revenue: {bank_leomi._bank_amount_of_revenue}")
    print(f"Bank Discount revenue: {bank_discount._bank_amount_of_revenue}")

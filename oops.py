class DigitalWallet:
    def __init__(self, initial_balance):
        # CHANGED: Used single underscore (_) so children can access it
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
            return True
        return False

    def pay(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Paid: {amount}")
            return True
        else:
            print("Payment Failed: Insufficient funds")
            return False

    def get_balance(self):
        return self._balance

class CreditCard(DigitalWallet):
    def __init__(self, initial_balance, credit_limit):
        super().__init__(initial_balance)
        self.credit_limit = credit_limit

    # Renamed to avoid conflict with the variable 'credit_limit'
    def increase_amount(self, amount):
        if amount > 0:
            self.credit_limit += amount
            print(f"Limit increased. New Amount: {self.credit_limit}")

    # OVERRIDING the parent's pay method
    def pay(self, amount):
        # Calculate total available funds (Cash + Credit)
        available_funds = self._balance + self.credit_limit
        
        if 0 < amount <= available_funds:
            # We can access _balance because it is Protected (not Private)
            self._balance -= amount 
            print(f"Credit Card Payment: {amount} accepted.")
            return True
        else:
            print("Payment Failed: Over limit!")
            return False

# # --- Testing ---
# my_card = CreditCard(50000, 100000) # Balance 50000, Limit 100000

# print(f"Start Balance: {my_card.get_balance()}")

# # Try to spend 800 (more than balance, but within limit)
# my_card.pay(80000)

# print(f"End Balance: {my_card.get_balance()}") 
# # Balance should be -300 now (which is okay for credit cards!)
list1 = [DigitalWallet(1000), CreditCard(2000, 50000)]
for Wallet in list1:
    Wallet.pay(10000)
    print(f"Remaining Balance: {Wallet.get_balance()}")
from abc import ABC, abstractmethod
class paymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class Paypal(paymentMethod):
    pass
p = Paypal()
p.pay(100)
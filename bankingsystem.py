from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit(self, amount): pass
    @abstractmethod
    def withdraw(self, amount): pass
    @abstractmethod
    def get_balance(self): pass
    @abstractmethod
    def transfer(self, amount, target_account): pass

class Account(Bank):
    def __init__(self, name, initial_balance=0):
        self.name = name  # Added a Name so we know who owns the account
        self._balance = initial_balance

    # --- THE MAGIC METHOD ---
    def __str__(self):
        # This tells Python what to return when you run print(account_object)
        return f"Account({self.name})"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            # We don't print here anymore to keep the output clean during transfers
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("❌ Error: Insufficient funds.")

    def get_balance(self):
        return f"💰 {self.name}'s Balance: ${self._balance}"
    
    def transfer(self, amount, target_account):
        if 0 < amount <= self._balance:
            self._balance -= amount
            target_account.deposit(amount)
            # Notice how {target_account} now uses the __str__ method we wrote!
            print(f"✅ Success: Transferred ${amount} from {self.name} to {target_account}")
        else:
            print("❌ Transfer Failed: Insufficient funds.")

# --- EXECUTION ---
person1 = Account("Alice", 100000)
person2 = Account("Bob", 50000)

print(f"Before: {person1.get_balance()} | {person2.get_balance()}")
print("-" * 50)

person1.transfer(45000, person2)

print("-" * 50)
print(f"After:  {person1.get_balance()} | {person2.get_balance()}")
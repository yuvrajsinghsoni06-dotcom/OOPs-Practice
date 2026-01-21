from abc import ABC , abstractmethod
class Paymethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class Creditcard(Paymethod):
    def __init__(self,card_limit):
        self._limit = card_limit
    def pay(self,amount):
        if self._limit >= amount:
            self._limit -= amount
            return f"Credit card Approved! Paid ${amount}. Remaining amount ${self._limit}. "
        else:
            return f"Credit Card Declined! Over Limit."
class PayPal(Paymethod):
    def __init__(self, current_balance):
        self._balance = current_balance
        
    def pay(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return f"PayPal success! Paid ${amount}. New Balance: ${self._balance}"
        else:
            return f"PayPal failed. Insufficient funds."
class Checkout:
    def __init__(self):
        self._total = 0  # here why i have not initialized total peremter
    def add_item(self, price):
        self._total += price
    def process(self, payment_method):
        print(f"Total to pay: ${self._total}")
        result = payment_method.pay(self._total) # what does this do explain me ??
        print(result)
#test case:.....
# Scenario 1: Paying with Credit Card
my_card = Creditcard(card_limit=5000) # Logic for card is inside the card object
register = Checkout()
register.add_item(100)
register.add_item(50)

print("--- Transaction 1 ---")
register.process(my_card) 

# Scenario 2: Paying with PayPal
my_wallet = PayPal(current_balance=20) # Poor guy only has $20
register2 = Checkout()
register2.add_item(100)

print("\n--- Transaction 2 ---")
register2.process(my_wallet)






        

       


            


   


    
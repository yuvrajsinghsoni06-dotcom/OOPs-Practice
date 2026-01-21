class VendingMachine: # No need for ABC yet, let's keep it concrete
    def __init__(self, product_name, price,inventory_count):
        # STATE: Held internally
        self._product_name = product_name
        self._price = price
        self._balance = 0  # Machine starts with 0 money inserted
        self._inventory_count = inventory_count

    def insert_coin(self, amount):
        # BEHAVIOR: Modifies state safely
        if amount <= 0:
            print("Invalid coin.")
            return
        self._balance += amount
        print(f"Debug: Inserted ${amount}. Current Balance: ${self._balance}")

    def buy_product(self):
        # BEHAVIOR: Checks internal state to make a decision
        if self._balance >= self._price:
            change = self._balance - self._price
            self._inventory_count -= 1
            self._balance = 0  # Reset balance after purchase
            print(f"SUCCESS: Dispensing {self._product_name}...")
            print(f"Returning change: ${change}")
            return True
        elif self._inventory_count == 0:
            amount_return = self._balance
            print(f"Sorry inventory is empty")
            print(f"Here is your Money : {amount_return}")
            return False
        else:
            needed = self._price - self._balance
            print(f"FAILURE: Insufficient funds. Please insert ${needed} more.")
            return False

    
    
    

    
        

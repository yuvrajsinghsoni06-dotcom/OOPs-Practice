class Expense:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
    
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self,new_amount):
        if new_amount < 0:
            raise ValueError("Amount cannot be negative")
        else:
            self._amount = new_amount

    def __str__(self):
        return f"Expense: {self.name} has Amount: {self.amount}"
    
    def __gt__(self,other):
        return self.amount > other.amount
    
    def __add__(self,other):
        if isinstance(other,Expense):
            return self.amount + other.amount
        elif isinstance(other , (int,float)):
            return self.amount + other
        else:
            return NotImplemented

class Wallet:
    def __init__(self):
        self.expenses = []

    def add_expense(self,expense):
        self.expenses.append(expense)
        print(f"Added expense: {expense} to wallet")
    def __len__(self):
        return len(self.expenses)
    def __getitem__(self,index):
        return self.expenses[index]
    
wallet = Wallet()
wallet.add_expense(Expense("Rent" , 25000))
wallet.add_expense(Expense("Food" , 1500))
print(f"Total number of expenses in wallet: {len(wallet)}")
print(f"First exxpense in wallet: {wallet[0]}")        

        
    
e1 = Expense("Tax" , 500000000)
e2 = Expense("Gym" , 200000)
print(e1)
if e1 > e2:
    print(f"{e1.name} is more expensive than {e2.name}")
total_cost = e1 + e2
print(f"Total Expense Amount: {total_cost}")
new_total = e1 + 500000000000000
print(new_total)
for expense in wallet:
    calculate_total = 




from abc import ABC, abstractmethod

# --- Abstract Interface ---
class Bank(ABC):
    @abstractmethod
    def action(self): 
        pass
    
    @abstractmethod
    def power(self): 
        pass
    
    @abstractmethod
    def salary_desc(self): 
        pass

# --- Base Data Class ---
class Employees():
    def __init__(self, name, empid, status, salary):
        self._name = name
        self._empid = empid
        self._status = status
        self._salary = salary

    def __str__(self):
        return (f"--- {self._status} Profile ---\n"
                f"Name: {self.name} | ID: {self._empid}\n"
                f"Action: {self.action()}\n"
                f"Power:  {self.power()}\n"
                f"Income: {self.salary_desc()}")

    @property
    def name(self):
        return self._name.title() 
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        # FIX 1: Use '>' instead of '>=' so we don't block the next condition
        if new_salary > 0:
            self._salary = new_salary
        elif new_salary == 0:
            print("⚠️ Warning: Setting salary to 0. Are you sure they are a volunteer?")
            self._salary = new_salary
        else:
            # This raises an error, which we must catch in the main code
            raise ValueError("Salary cannot be negative")

# --- Concrete Implementations ---

class Manager(Employees, Bank):
    def __init__(self, name, empid, salary):
        super().__init__(name, empid, "Manager", salary)

    def action(self):
        return "Approves loans and manages the team."
    
    def power(self):
        return "High Level: Vault Access + System Control."
    
    def salary_desc(self):
        return f"${self._salary} + Annual Bonuses"

class FullTimeEmployee(Employees, Bank):
    def __init__(self, name, empid, salary):
        super().__init__(name, empid, "Full-Time", salary)

    def action(self):
        return "Processes loans and assists customers."
    
    def power(self):
        return "Moderate Level: Transaction processing."
    
    def salary_desc(self):
        return f"${self._salary} (Standard Base)"

class Intern(Employees, Bank):
    def __init__(self, name, empid, salary):
        super().__init__(name, empid, "Intern", salary)

    def action(self):
        return "Assists staff and learns operations."
    
    def power(self):
        return "Low Level: Common areas only."
    
    def salary_desc(self):
        return f"${self._salary} (Stipend)"

class Contractor(Employees, Bank):
    def __init__(self, name, empid, salary):
        super().__init__(name, empid, "Contractor", salary)

    def action(self):
        return "Specialized IT or Security maintenance."
    
    def power(self):
        return "Restricted: Limited to contract terms."
    
    def salary_desc(self):
        return f"${self._salary} (Per Contract)"

# --- Main Execution ---

emp1 = Intern("John Doe", 12345, 15000)
print(f"Current Salary: {emp1.salary}")

print("\n...Updating Salary to 20,000...")
emp1.salary = 20000
print(emp1)

print("\n...Updating Salary to 0...")
emp1.salary = 0  # This should now trigger the Warning print!
print(emp1)

print("\n...Updating Salary to -5,000...")

# FIX 2: We use try/except to handle the crash gracefully
try:
    emp1.salary = -5000 
except ValueError as e:
    print(f"🚫 BLOCKED: {e}") 

# Prove the salary didn't change to negative
print(f"Final Salary Check: ${emp1.salary}")
class TipCalculator:
    def __init__(self, total_bill, tip_percentage, num_people):
        self.total_bill = total_bill
        self.tip_percentage = tip_percentage
        self.num_people = num_people

    def calculate_tip(self):
        # Calculate tip and update the total bill
        tip_amount = self.total_bill * (self.tip_percentage / 100)
        self.total_bill += tip_amount
        return f" Total bill with tip: ${self.total_bill:.2f}"

    def split_bill(self, requests):
        if requests == "yes":
            amount_per_person = self.total_bill / self.num_people
            return f" Per person amount: ${amount_per_person:.2f}"
        else:
            return f" Total amount: ${self.total_bill:.2f}"

    def __str__(self):
        # This triggers the input when you try to 'print' the object
        return self.split_bill(input("Do you want to split the bill ? Type 'yes' or 'no': "))

if __name__ == "__main__":
    print("=== Tip Calculator ===")
    bill_amount = float(input("What was the total bill? $"))
    tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    num_people = int(input("How many people to split the bill? "))
    
    calculator = TipCalculator(bill_amount, tip_percent, num_people)
    calculator.calculate_tip() 
    print(calculator)
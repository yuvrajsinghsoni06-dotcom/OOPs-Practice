class TipCalculator:
    def __init__(self, total_bill, tip_percentage, num_people):
        self.total_bill = total_bill
        self.tip_percentage = tip_percentage
        self.num_people = num_people
        self.final_amount = 0

    def calculate_tip(self):
        tip_amount = self.total_bill * (self.tip_percentage / 100)
        self.final_amount = self.total_bill + tip_amount
        return f"Total bill with tip: ${self.final_amount:.2f}"

    def split_bill(self, requests):
        if self.num_people <=0:
            return f" Cannot split bill among zero or negative people."
        amount_to_split = self.final_amount if self.final_amount > 0 else self.total_bill
        if requests == "yes":
            amount_per_person = self.final_amount / self.num_people
            return f"Per person amount: ${amount_per_person:.2f}"
        else:
            return f"Total amount: ${amount_to_split:.2f}"
    def __str__(self):
        current_total = self.final_amount if self.final_amount > 0 else self.total_bill
        return f"Bill Summary: ${current_total:.2f} split among {self.num_people} people."
person1 = TipCalculator(1500.90, 23, 5)


print(person1.calculate_tip()) 


print(person1.split_bill("yes"))


print(person1)
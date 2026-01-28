class TipCalculator:
    def __init__(self, total_bill, num_people):
        self.total_bill = total_bill
        self.num_people = num_people
        self.final_amount = total_bill # Initialize with bill amount
        self.suggested_tip_percent = 0 
        self.input_tip = 0


    def get_service_recommendation(self, rating):
        if rating == 1:
            self.suggested_tip_percent = 5
            return "Sorry for the poor service. Suggesting 5% tip."
        elif rating == 2:
            self.suggested_tip_percent = 10
            return "Good service! Suggesting 10% tip."
        elif rating == 3:
            self.suggested_tip_percent = 15
            return "Excellent service! Suggesting 15% tip."
        else:
            self.suggested_tip_percent = 0
            return "Invalid rating."

    def calculate_tip(self, apply_tip):
        if apply_tip == "yes":
            while True:
                try:
                    user_input = input(f"Enter tip percentage (suggested {self.suggested_tip_percent}%): ")
                    self.input_tip = float(user_input)  
                    break  
                except ValueError:
                    print("Invalid input! Please enter a number (e.g., 10 or 15).")
            tip_amount = self.total_bill * (self.input_tip / 100)
            self.final_amount = self.total_bill + tip_amount
        return f"Bill with tip: ${self.final_amount:.2f}"

    def special_offer(self):
        if self.total_bill > 2000:
            discount = self.total_bill * 0.05
            self.final_amount -= discount
            return f"Loyalty Discount Applied: -${discount:.2f}"
        return "No discount applicable."

    def split_bill(self, split_request="yes"):
        if self.num_people <= 0:
            return "Error: Cannot split by zero."
        if split_request == "yes":
            amount_per = self.final_amount / self.num_people
            return f"Per person: ${amount_per:.2f}"
        return f"Total: ${self.final_amount:.2f}"

# --- Execution ---
order = TipCalculator(2500, 5) # Testing with > 2000 for the discount
print(order.get_service_recommendation(3))
print(order.calculate_tip("yes"))
print(order.special_offer())
print(order.split_bill("no"))





        
        


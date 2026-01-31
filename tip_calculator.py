class TipCalculator:
    def __init__(self, total_bill, num_people):
        self.total_bill = total_bill
        self.num_people = num_people
        self.final_amount = total_bill 
        self.suggested_tip_percent = 0 
        self.input_tip = 0
        self.tip_amount_val = 0

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
            return "We Apologize for our Service."

    def calculate_tip(self, apply_tip):
        if apply_tip == "yes":
            while True:
                try:
                    user_input = input(f"Enter tip percentage (suggested {self.suggested_tip_percent}%): ")
                    self.input_tip = float(user_input)  
                    break  
                except ValueError:
                    print("Invalid input! Please enter a number.")
            
            # Store the calculated tip amount so we can access it later
            self.tip_amount_val = self.total_bill * (self.input_tip / 100)
            self.final_amount = self.total_bill + self.tip_amount_val
        return f"Bill with tip: ${self.final_amount:.2f}"

    def special_offer(self):
        if self.total_bill > 2000:
            discount = self.total_bill * 0.05
            self.final_amount -= discount
            return f"Loyalty Discount Applied: -${discount:.2f}"
        else:
          return f"No discount applicable."

    def split_bill(self, split_request="yes"):
        if self.num_people <= 0:
            return "Error: Cannot split by zero."
        if split_request == "yes":
            amount_per = self.final_amount / self.num_people
            return f"Per person: ${amount_per:.2f}"
        return f"Total: ${self.final_amount:.2f}"


def main():
    # --- 1. Initialize Shift Stats ---
    total_volume = 0.0
    total_tips_collected = 0.0
    customer_served = 0

    print("--- Shift Started ---")

    while True:
        user = input("\nEnter bill amount (or 'exit' to finish): ")
        
        # --- Fix 1: Correct Exit Logic ---
        if user.lower() in ["exit", "q"]:
            break
        
        try:
            bill_amount = float(user)
            
            # --- Fix 3: Instantiate and Use the Class ---
            # 1. Create the object
            my_calc = TipCalculator(bill_amount,1)  # Default to 1 person for simplicity
            
            # 2. Run the logic (simulating a quick flow for the loop)
            # You can ask for rating/people here if you want, 
            # but for now let's just assume standard flow:
            
            # Rate service
            print(my_calc.get_service_recommendation(input("Rate service (1-Poor, 2-Good, 3-Excellent): "))) 
            
            # Calculate Tip
            print(my_calc.calculate_tip(input("Would you like to add a tip? (yes/no): ").lower()))
            
            # Check Special Offer
            print(my_calc.special_offer())
            
            # --- Update Stats (The Bonus) ---
            # We add this specific customer's data to the shift totals
            total_volume += bill_amount
            total_tips_collected += my_calc.tip_amount_val
            customer_served += 1
            
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

    # --- End of Shift Report ---
    print("\n" + "="*30)
    print("       SHIFT REPORT       ")
    print("="*30)
    print(f"Total Customers: {customer_served}")
    print(f"Total Volume:    ${total_volume:.2f}")
    print(f"Total Tips:      ${total_tips_collected:.2f}")
    
    if total_volume > 0:
        avg_tip_percent = (total_tips_collected / total_volume) * 100
        print(f"Avg Tip %:       {avg_tip_percent:.1f}%")
    else:
        print("Avg Tip %:       0.0%")
    print("="*30)

if __name__ == "__main__":
    main()
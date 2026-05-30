class TipCalculator:
    def __init__(self, total_bill: float, num_people: int):
        self.total_bill = total_bill
        self.num_people = num_people
        self.final_amount = total_bill 
        self.suggested_tip_percent = 0 
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

    def calculate_tip(self,tip_percentage: float):
            self.tip_amount_val = self.total_bill * (tip_percentage / 100)
            self.final_amount = self.total_bill + self.tip_amount_val
            return f"Bill with tip: ${self.final_amount:.2f}"

    def special_offer(self):
        if self.total_bill > 2000:
            discount = self.total_bill * 0.05
            self.final_amount -= discount
            return f"Loyalty Discount Applied: -${discount:.2f}"
        else:
            return f"No discount applicable."

    def split_bill(self, split_response: str):
        if self.num_people <= 0:
            return "Error: Cannot split by zero."
        if split_response == "yes":
            amount_per = self.final_amount / self.num_people
            return f"Per person: ${amount_per:.2f}"
        return f"Total: ${self.final_amount:.2f}"
    

    def to_pay(self):
        return f"Final Bill to pay : {self.final_amount:.2f}"

    def complementary_gift(self):
        # [FIX] Reordered logic: Check the higher value (500) FIRST.
        # If we checked >= 100 first, 600 would get stuck there.
        if self.tip_amount_val > 500:
             # [FIX] Corrected typo: 'tip_amount_value' -> 'tip_amount_val'
            return "Chance to participate in lucky Draw and have a chance for yourself to make today's meal on the House"
        elif self.tip_amount_val >= 100:
            return "A Special Sweet dish"
        else:
            return "Thank you for visiting!"

def main():
    # --- 1. Initialize Shift Stats ---
    total_volume = 0.0
    total_tips_collected = 0.0
    
    # [FIX] Renamed accumulator to avoid confusion with loop input
    total_customers_served_shift = 0 

    print("--- Shift Started ---")

    while True:
        user_bill = input("\nEnter bill amount (or 'exit' to finish): ")
        user_input = input("Enter Tip % :  ")
        split_response = input("Split the bill? (yes/no): ").lower()
        # [FIX] Check exit BEFORE asking for number of people
        try:
            tip_val =float(user_input)
        except ValueError:
            print("Invalid tip percentage! Please enter a valid number.")
            continue
        if user_bill.lower() in ["exit", "q"]:
            break

        # [FIX] Use a distinct variable name for the input
        people_input = input("Enter No of people dining: ")
        
        try:
            bill_amount = float(user_bill)
            
            # [FIX] Convert people input to int immediately
            total_people_table = int(people_input)
            
            # 1. Create the object
            my_calc = TipCalculator(bill_amount, total_people_table)
            
            # 2. Rate service
            rating_input = input("Rate service (1-Poor, 2-Good, 3-Excellent): ")
            if rating_input.isdigit():
                print(my_calc.get_service_recommendation(int(rating_input)))
            else:
                print("Invalid rating, skipping suggestion.")
            
            # 3. Calculate Tip
            print(my_calc.calculate_tip(tip_val))
            
            # 4. Check Special Offer & Pay
            print(my_calc.special_offer())
            print(my_calc.to_pay())

            print(my_calc.split_bill())
            print(my_calc.complementary_gift())
            
            # --- Update Stats ---
            total_volume += bill_amount
            total_tips_collected += my_calc.tip_amount_val
            
            # [FIX] Accumulate correctly using the separate variables
            total_customers_served_shift += total_people_table
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

    # --- End of Shift Report ---
    print("\n" + "="*30)
    print("       SHIFT REPORT       ")
    print("="*30)
    print(f"Total Customers: {total_customers_served_shift}")
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
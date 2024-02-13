# Code Like A Girl - Assignment 3 (alt script)
# Name: Ruby Saint
# Date: 13/02/2024
# Notes: Wanted to mess around with/practice setting up script using the class() method! I don't really understand how it works yet, but am keen to try and familliarise myself with the structure :) 

class Savings_Calc():
    def __init__(self):
        self.money_start = float(input("Starting balance: "))
        self.saving_years = int(input("Number of years: "))
        self.interest_rate = input("Interest rate: ")
    
    def run(self):
        self.validate_input()
        self.calc_increase()

    def validate_input(self):
        # Wanted to try and check for '%' symbols in the interest rate user input (for fun/to see if I could get it working). Ended up just checking that all chars are numeric. 
        # Not too sure how to work with exceptions yet so I'm relying on line 21 throwing a type error if it contains non-allowed chars. 
        if not self.interest_rate.isnumeric():
            print("Error: please provide interest rate as a floating point value (percentage symbols and other special chars should be omitted)")
        self.int_rate_number = float(self.interest_rate)    

    def calc_increase(self):
        money_result = self.money_start * self.int_rate_number * self.saving_years
        print(f"Your savings after {self.saving_years} years: ${money_result}")
        afford_holiday = money_result > 10000
        print(f"Will you be able to afford your holiday? {afford_holiday}")

def main(): 
    Savings_Calc().run()

if __name__ == '__main__': 
    main()
# Code Like A Girl - Assignment 3: Savings Calculator  
# Name: Ruby Saint
# Date: 13/02/2024

money_start = float(input("Starting balance: "))
saving_years = float(input("Number of years: ")) # Could probably be int or float - opted to use float to allow more flexibility
interest_rate = float(input("Interest rate: "))

money_result = (money_start*interest_rate)*saving_years # Brackets don't impact order of operations here, just makes more sense in my head to read it this way!

print(f"Your savings after {saving_years} years: ${round(money_result)}") # Used round() instead of int() to give a whole number but rounded up or down as usual

afford_trip = money_result>10000
print(f"Will you be able to afford your holiday? {afford_trip}") 

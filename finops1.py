#finops v1. A simple finance tool to calculate simple interest or compound interest.

print("Welcome to finops!")
print("                 ")

#Ask the user the type of calculation they want

calculation_type = input("What would you like to calculate? (Simple/Compound): ").lower()

#collect required input
principal = float (input("Enter the principal amount: $"))
rate = float (input("Enter the annual interest rate (%): "))
time = float (input("Enter the time period in years: "))

#perform the calculations based on choice of the user.
if calculation_type == "simple":
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    print(f"\nSimple Interest is $ {simple_interest: .2f}")
    print(f"Total amount after {time} years is ${total_amount: .2f}")
    print("Thank you for using finops!")

elif calculation_type == "compound":
    n = int(input("Enter number of times interest is compounded per year: "))
    total_amount = principal * (1 + (rate / (100 * n))) ** (n * time)
    compound_interest = total_amount - principal
    print(f"\nCompound Interest is $ {compound_interest: .2f}")
    print(f"Total amount after {time} years is ${total_amount: .2f}")
    print("Thank you for using finops!")

else:
    print("Invalid option. Please choose either Simple or Compound.")
    print("Thank you for using finops!")
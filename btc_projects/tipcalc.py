# Getting input from the user for the bill amount, tip percentage, and number of people
bill_amount = float(input("What is the bill amount: "))
tip_percentage = int(input("Select the tip percentage (e.g., 10, 12, 15, 20): "))
split_people = int(input("Select the number of people to share the bill: "))

# Calculating the total amount including the tip
total_amount = bill_amount * (1 + tip_percentage / 100)

# Calculating the amount each person should pay
amount_per_person = total_amount / split_people

# Rounding the result to 2 decimal places
final_amount = round(amount_per_person, 2)

# Printing the final amount each person should pay
print(f"Each person should pay: ${final_amount:.2f}")

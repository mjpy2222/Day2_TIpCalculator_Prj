
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n"))
Tip_percentage = int(input("What tip percentage would you like to give?\n 10, 12, or 15\n"))
total_people = int(input("How many people are splitting the bill?\n"))

bill_with_tip = Tip_percentage / 100 * total_bill + total_bill

per_person_total = bill_with_tip / total_people

print(f"{per_person_total:.2f}")

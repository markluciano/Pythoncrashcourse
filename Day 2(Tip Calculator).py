#Banner for tip calculator
print("Welcome to the tip calculator!")
#What was total bill
bill= float(input("What was the total bill? $"))
#How much would you like to tip (calculation takes place)
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
#How many people to split the bill?
people =int(input("How many people to split the bill?"))
# How much each person should pay
bill_with_tip = tip /100 * bill + bill
tip_as_percent = tip /100
total_tip_amount = bill + tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: $" + str(final_amount))

#Line 12-13 need to be reworked (double counted the bill)
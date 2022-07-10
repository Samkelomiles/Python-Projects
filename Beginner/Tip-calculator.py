#=============DAY 2====================
#+++++++++++++++++++++++++++++++
#=================== TIP CALCULATOR SECTION =======================
print("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill: R"))
tip  = int(input("What percentage would you like to give (10,12 or 15) - "))
num_of_people = int(input("How many people to split the bill: "))

bill += bill*(tip/100)
bill_per_person = bill/num_of_people
split = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: R{split}")


#By: Sabria Fafach
#Date: Febuary, 2 2025
#Title: program_5.py

budgeted_amount=float(input("Enter the amount of money you have budgeted for the month in dollars:"))
expense=0
exp_int=input("Do you want to enter an expense?(enter y for yes):")
while exp_int=="y":
    expense=float(input("Enter your expense in dollars:"))+expense
    exp_int=input("Do you want to add another expense?(enter y for yes):")

difference=budgeted_amount-expense

if difference>0:
    print(f"You have ${difference:.2f} left for the month.")
elif difference<0:
    print(f"You have spent ${((difference)**2)**.5:.2f} more than you budgeted.")
else:
    print("You have broken even.")

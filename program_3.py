#By: Sabria Fafach
#Date: Febuary, 2 2025
#Title: program_3.py


rainfall=0
years=int(input("Enter a number of years:"))
for year in range(1,years+1):
    months=years*12
    for month in range(1,months+1):
        rainfall=float(input("Enter a number of inches of rain for this month:"))+rainfall

print(f"You entered data for {months} months.")
print(f"The total rainfall for all the months is {rainfall:0.0f} in.")


Ave_rainfall=rainfall/months
print(f"The average rainfall per month is in {Ave_rainfall:0.0f} in.")
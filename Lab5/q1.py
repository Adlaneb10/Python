#Prompt the user to enter a mark between 0 and 100 and to print
#This is a pass” if the mark is 40 or over, and 
# “This is a fail” if the mark is below 40. Hint: use >=
#Author: Adlane Boulmelh
# Date: 29/09/2020

#Ask user for input
mark_str = input("Enter your mark between 0 and 100: ")

# convert string to int
mark_int = int(mark_str)

# if + else statement to check whether entry is pass or fail
if mark_int >= 40:
    print("This is a pass")

else:
    print("This is a fail")
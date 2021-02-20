#Write a Python program that prompts for a number. 
# Take that number, add 2, multiply by 3, subtract 6, and divide by 3.
#  You should get the number you started with.
# Author: Adlane Boulmelh
#Date: 22/09/2020

number_str = input("Enter a number: ")

#Convert from string to int
number_int = int(number_str)

number_int = number_int + 2
number_int = number_int * 3
number_int = number_int - 6
number_int = int(number_int/3)

print("Your number is ",number_int)



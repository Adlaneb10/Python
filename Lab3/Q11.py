# (Integer operators) One way to determine whether an integer is 
# even is to divide the number by 2 and check the remainder. 
#Write a three-line program that prompts for a
#number, converts the input to an integer, and prints a 0 
#if the number is even and a 1 if the number is odd.

checker_int = int(input("Enter a number to check if it's odd or even:"))

#convert string to int


if checker_int % 2 == 0:
    print(" 0",)
else:
    print("1")

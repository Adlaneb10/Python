# Ask the user to enter a number and print it back on the screen.
#  Keep asking for a new number until they enter a negative number
num = 0

while(num > -1):
    num = int(input("Enter a negative number "))
    print("You entered ",num)

    if num < 0:
        print("Thank you")
        break
    

    
    



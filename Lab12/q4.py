#Program prompt for three nums

checker = 0

while checker == 0:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    try:
        total = (num1/num2) + num3
        print(total)
        checker += 1

    except ValueError:
        print("Error invalid entry try again")

    except ZeroDivisionError:
        print("Error invalid entry try again")

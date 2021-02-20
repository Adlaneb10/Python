#continue staement example

sum = 0
while True: # this loop wont end unless a break is there under
    number_str = input("Please enter a number: ")

    if number_str == ".":
        print("Final sum is: ", sum)
        break

    number = int(number_str)

    if number % 2 == 0:
        sum += number ## sum = sum + number
        continue
    elif number % 2 == 1:
        print("Number is not even! Enter even numbers only. ")
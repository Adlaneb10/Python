# algorithm collatz sequence

number = int(input("please enter a number: "))
count = 0

while number != 1:
    if number % 2 == 1:
        number = number *3 + 1
    else:
        number /=2

    number = int(number)
    print(number, end = " ")
    count += 1
else:
    print()
    print("Sequence is", count, "numbers long")
#get input
number_str = input("Please enter a number to check:")
number = int(number_str)

#calc sum of the divisors
divisor = 1
sum_of_divisors = 0
while divisor < number:
    if number%divisor == 0:
        sum_of_divisors = sum_of_divisors+divisor
    divisor = divisor + 1

#classify the result
if number == sum_of_divisors:
    print(number, "is perfect")
elif number < sum_of_divisors:
    print(number, "is not efficient")
elif number>sum_of_divisors:
    print(number,"is abundant")
    
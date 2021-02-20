#number_str = float(input("Enter a floating point number: "))
#i = 0

num = input("Enter a floating point number: ")

while True:

    try:
        num_float = float(num)
    except ValueError:
        num = input("Enter a float point num: ")
    else:
        break

print("number is ",num_float)


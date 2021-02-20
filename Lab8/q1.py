num = int(input("Enter number to convert to binary: "))

if num < 0:
    print("No negative numbers ")
if num == 0:
    print(num)
    exit()

binary =""

while num // 2 > 0:
    remainder = num % 2
    binary = binary + str(remainder)
    num = num // 2

remainder = num % 2
binary = binary + str(remainder)

binary = binary[::-1]

print(binary)


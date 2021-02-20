bin_str = input("Enter a binary number: ")

if int(bin_str) == "0" or bin_str[0] == "-":
    print("number not allowed")

exp = 0 
sum = 0

for i in range(len(bin_str) - 1,-1,-1):
    sum += int(bin_str[i]) * 2 ** exp
    exp += 1

print(sum)
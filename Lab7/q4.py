#Ask for input from user
my_str = input("Enter a string: ")

if len(my_str) < 4:
    print("length less than 4")
#Replace strings
my_str = my_str[0] + my_str[1] + my_str[-2] + my_str[-1]

print(my_str)
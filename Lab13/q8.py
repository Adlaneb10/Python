import string

string.ascii_lowercase

entry = input("Enter a string: ")

my_set = set(string.ascii_lowercase)
print(my_set)

if len(set(my_set) == 27:
    print("String is a pangram")

else:
    print("isnt")



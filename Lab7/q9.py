import string
#get input from user
my_str = input("Enter a string: ")

#lowercase all chars
my_str = my_str.lower()
i = 0
# you can use bad chars as well
#print(str.replace("'"," "))
bad_chars = string.whitespace + string.punctuation

for i in range(0,len(bad_chars)):
    #remove all bad chars
    my_str = my_str.replace(bad_chars[i]," ")


#checker for if reverse string equal normal string
if my_str == my_str[::-1]:
    print("Reverse is equal to string ")
else:
    print("Reverse is not equal to orginal string")






def string(str1):
    if len(str1) < 4:
        print("length less than 4")
    #Replace strings
    else:
        str1 = str1[0] + str1[1] + str1[-2] + str1[-1]
        print(str1)
    return str1

entry = input("Enter a string: ")
string(entry)


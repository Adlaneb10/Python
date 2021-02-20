def remove_sub(my_str,ind1,ind2):
    if ind1 < ind2:
        print(ind1,"is greater than ",ind2)
        return my_str

    result = my_str[:ind1] + my_str[ind2+1:]
    return result

sent = input("input a sentence: ")
ind1 = int(input("Enter the first index less than " + str(len(sent)-1)+ ": "))
ind2 = int(input("input index less than " + str(len(sent)) + \
    " and greater than" + str(ind1) + ": "))

print(remove_sub(sent,ind1,ind2))
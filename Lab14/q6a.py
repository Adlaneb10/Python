# Write a function that takes a list of integer as an argument,
# removes even number from the list and returns modified list.
# Author: Adlane Boulmelh
import string


def remove_even(my_list):
    list_new = []
    print("PART A\n")
    for i in my_list:
        #if odd num is found it will append to new list
        if i % 2 == 1:
            list_new.append(i)
    return list_new

list1 = [1,2,3,4,5,6]

list1 = remove_even(list1)

print(list1)

#b
def remove_odd(odd_list):
    print("PART B\n")
    list_new1 = []
    for i in odd_list:
        #if even number is found it will be appended to new list
        if i % 2 == 0:
            list_new1.append(i)

    return list_new1


list2 = [1,2,3,4,5,6]

list2 = remove_odd(list2)

print(list2)

#c
def remove_c(c_list):
    # Change between false or true
    bool = True
    list_new1 = []
    list_new1 = []
    print("PART C\n")
    if bool is True:
        for i in c_list:
            if i % 2 == 1:
                list_new1.append(i)

        return list_new1
        #del c_list[1::2]

    if bool is False:
        for i in c_list:
            if i % 2 == 0:
                list_new1.append(i)
        return list_new1
list3 = [1,2,3,4,5,6]
list3 = remove_c(list3)
print(list3)

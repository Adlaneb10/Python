def diff(list1,list):
    list_diff = []
    for el in list1:
        if el not in list2:
            list_diff.append(el)

    return list_diff

list1 = [1,2,3,4,5,6]
list2 = [10,9,8,7,6]

print(diff(list2,list1))
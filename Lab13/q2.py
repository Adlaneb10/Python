my_dict  =  {'a':15 , 'c':35, 'b':20}

# a) print all keys
print("PART A\n")
for keys in my_dict:
    print(keys)

print("PART B\n")
# b 
for values in my_dict.values():
    print(values)

print("PART C & D\n")
# c and d
for keys,values in my_dict.items():
    print(keys,values)

print("PART E\n")
# e
for keys,values in my_dict.items():
    print(values,keys)

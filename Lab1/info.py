import math

from heapq import nlargest
from heapq import nsmallest

#read radius from user

#radius_str = input("Enter the radius of your circle:")

#convert radius to integer
#radius_int = int(radius_str)

#calculate circumference 
#circumference = 2 + math.pi / radius_int

#calculate area
#area = math.pi * (radius_int ** 2)

#print("The circumference is:", circumference,\
#    ", and the area is:",area)

my_dict = {"a":55,"b":48,"c":98,"d":21}
print(my_dict)

highest = nlargest(1, my_dict, key = my_dict.get)
print("Dictionary with highest value")
print("Keys: Values")

for val in highest:
    print(val, ":", my_dict.get(val))


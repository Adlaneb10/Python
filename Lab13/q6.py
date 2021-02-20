capitals = {}

list1 = [0,1,3,4]



list1[0] = input("Enter Country: ")
list1[1] = input("Enter Country: ")
list1[2] = input("Enter Country: ")
list1[3] = input("Enter Country: ")

print(list1)
capitals[0] = list1[0]
capitals[1] = list1[1]
capitals[2] = list1[2]
capitals[3]= list1[3]

city1 = input("Enter the city for country 1: ")
city2= input("Enter city 2: ")
city3 = input("Enter city 3: ")
city4 = input("Enter city 4: ")

capitals[city1] = capitals.pop(0)
capitals[city2] = capitals.pop(1)
capitals[city3] = capitals.pop(2)
capitals[city4] = capitals.pop(3)

print(capitals)

#Do again sort capital values in order

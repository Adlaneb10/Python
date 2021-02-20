#Generate a list of square numbers
list1 = []
sqr_num = int(input("How many square numbers do you want? : "))
for i in range(sqr_num):
    list1.append(i)

for i in range(0,sqr_num):
    list1[i] = list1[i] ** 2

print("PART A\n")
print(list1)


# Part B
print("PART B\n")
list_colours = ["Red","Blue","Green","Black","White"]

out = map(lambda x:x.upper(),["Red","Blue","Green","Black","White"])

list1 = list(out)
print(list1)

#part c
print("PART C\n")
count = 0


for j in range(1,1001):
    if j % 7 == 0:
        count += 1

print("There are ", count ," numbers that are divisble by 7 ")

list_new = []
count1 = 0
#part d
y = []
y = [y for y in range(1, 1000) if '7' in str(y)]
print("PART D\n")
print(y)

print("There are ", count1 ," numbers that have 3 in them ")

#part e
print("\nPART E\n")
space_count = 0
find_str = "Hello world"

if find_str == " ":
    space_count += 1

#print(find_str.count(" "))
print(space_count)


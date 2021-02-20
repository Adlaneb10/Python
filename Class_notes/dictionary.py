# Creat a dictionary using {} 
contacts = {'bill':'353-1234','richard':'123-4567','Adlane':'087-3807265'}
#print element of a dictionary
print(contacts["bill"])


#declaring empty dictionary
new_dict = {}

#assignment of new key in to empty list
new_dict["bill"] = 48

print(new_dict)

#bill -> '353-1234'
#richard -> 123-4567
#Adlane -> 0873807265


# Keys have to be unique

#print num of keys
print(len(contacts))

if "bill" in contacts:
    print("true")

for key in contacts:
    print(contacts)

#update element in dictions
contacts.update({"bill":"465-1111"})
print(contacts["bill"])

print(contacts.items())
#print(contacts.keys())
#print(contacts.values())


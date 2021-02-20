# class to represent a gym. Gym should have members name, DOB, height, weight
# most used equipment sub class
#Author: Adlane Boulmelh
#Date: 30/11/2020

class Gym_members(object):
    def __init__(self, gym_id = 0,name = "",age = 0, dob = "",height = 0, weight = 0):
        self.gym_id = gym_id
        self.name = name
        self.age = age
        self.dob = dob
        self.height = height
        self.weight = weight

    def __str__(self):
        print("in gym member class")
        result_str = "ID {}| Name {}| Age {}| DOB {}| Height {}cm| Weight {}kg|".format(self.gym_id,self.name,self.age,self.dob,self.height,self.weight)
        return result_str
class sub_gym(Gym_members):
    def __init__(self, gym_id = 0,name = "",age = 0, dob = "",height = 0, weight = 0,fav_item = ""):
        Gym_members.__init__(self,gym_id,name,age,dob,height,weight)
        self.fav_item = fav_item

    def __str__(self):
        print("in sub string class")
        result_str = Gym_members.__str__(self)
        result_str += "Favourite item is {}".format(self.fav_item)
        return result_str

#member1 = Gym_members(10,"Adlane", 19, "25/08/2001", 186, 74)
#print(member1)
member2 = sub_gym(10,"Adlane", 19, "25/08/2001", 186, 74,"Dumbells")
print(member2)

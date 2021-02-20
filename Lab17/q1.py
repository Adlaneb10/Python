# Design a class and a subclass, base class stores model car, model year,
# mileage, VIN, Engine size, transmission and colour.
# Add a subclass to state whether it is a Car, truck, SUV and minivan
#Author: Adlane Boulmelh
#Date 30/11/2020


#main class
class Base(object):
    def __init__(self, brand = "",
                 year = 0,
                 mileage = 0,
                 vin = "A123H456LTVY48TPW",
                 engine_size = "",
                 transmission = "",
                 colour = ""):
        self.brand = brand
        self.year = year
        self.mileage = mileage
        self.vin = vin
        self.engine_size = engine_size
        self.transmission = transmission
        self.colour = colour

    def compare_mileage(self):
        """ method to compare mileage of two vehicles"""
        mileage1 = car1.mileage
        mileage2 = car2.mileage
        #car1 = car1.brand
        #car2 = car2.brand
        #car1 += "has less mileage"
        #car2 += "has less mileage"
        if mileage1 << mileage2:

            return car1.brand + " has less mileage"
        else:
            return car2.brand + " has less mileage"

    def __str__(self):
        print("in base class str")
        result_str =  "Vehicle brand is {} . Year is {}. Mileage is {}\n VIN is {}. Engine Size is {}. Transmission is {}. Colour is {}\n ".format(self.brand, self.year, self.mileage,self.vin,self.engine_size,self.transmission,self.colour)
        return result_str

#Sub class
class car_type(Base):
    def __init__(self,brand = "",
                 year = 0,
                 mileage = 0,
                 vin = "A123H456LTVY48TPW",
                 engine_size = "",
                 transmission = "",
                 colour = "",
                 type_veh = ""):
        Base.__init__(self,brand,year,mileage,vin,engine_size,transmission,colour)
        self.type_veh = type_veh

    def __str__(self):
        print("In type string")
        #Assign string from base into var result_str
        result_str = Base.__str__(self)
        # add new string to base string
        result_str = result_str + "\nThis is a {}".format(self.type_veh)
        #return
        return result_str

#This will return string from Base class of vehicle info
car1 = car_type("Audi", 2019,10000,"B1234","2598cc","Automatic","Blue")
#print(car1)

#This will print Class base with the string from Class Type. On what type of vehicle it is
car2 = car_type("golf", 2020,20000,"A1234","1988cc","Manual","Blue", "car")
print(car2)

print(car2.compare_mileage())

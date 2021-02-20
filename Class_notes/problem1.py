#Program to solve rainfall problem

#calculate rainfall in liters of some number of cm on 1 acre 
cm_str=input("How many cm of rain has fallen:")
cm_int = int(cm_str)
#cm of depth (0.01 meters) * 1 acre of area(4046.86 square meters)
volume = cm_int * 0.01 * 4046.86
#convert vol in cubic metres to litres
litres = volume * 1000
print(cm_int,"Cm rain on 1 acre is", litres,"litres")

a_float = 2.5
a_int = 7
b_int = 6
print(a_int / b_int) # Line 1

print(a_int//a_float)

print(a_int % b_int)

print(int(a_float))
print(float(a_int))
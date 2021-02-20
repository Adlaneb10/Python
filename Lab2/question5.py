#make a program to calculate and print the area of a rectangle
#A = w*l 
#Author: Adlane Boulmelh

length_str = input("What is the length of your rectangle: ")

width_str = input("What is the width of your rectangle: ")

#convert from string to int
length_int = int(length_str)
width_int = int(width_str)
area = width_int * length_int

print("Area of rectangle is", area, \
    "\n Width entered is",width_int, \
        "\n Length entered is", length_int)



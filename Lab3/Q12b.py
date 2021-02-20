# Body mass index (BMI) is a number calculated from a person’s weight and height.
#According to the Centers for Disease Control and Prevention, the BMI is a fairly
#reliable indicator of body fatness for most people. BMI does not measure body fat
#directly, but research has shown that BMI correlates to direct measures of body fat,
#such as underwater weighing and dual-energy X-ray absorptiometry. The formula for
#BMI is
#weight / height²
#where weight is in kilograms and height in meters.
#(a) Write a program that prompts for metric weight and height and outputs the BMI.
#(b) Write a program that prompts for weight in pounds and height in inches, converts
#the values to metric, and then calculates the BMI.
#Author: Adlane Boulmelh
#Date: 22/09/2020

#Conversion pound to kg --> 1lbs = 0.45359237kg *
#conversion inches to meters i * 0.0254

#Prompt user for details
weight_str = input("Enter your weight in lbs")

height_str = input("Enter your height in inches")

#convert from string to float
weight_float = float(weight_str)
height_float = float(height_str)

weight_kg = weight_float * 0.45359237

height_m = height_float * 0.0254

print("Your weight in KG is ",weight_kg,\
    "Your height in meters is ",height_m)
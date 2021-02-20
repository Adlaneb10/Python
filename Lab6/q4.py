#Write a program to calculate and print the factorial of a number using
#  a FOR loop. The factorial of a number is the product of all 
# integers up to and including thatnumber, 
# so the factorial of 4 is 4*3*2*1= 24

num = input("Enter your number: ")
num_int = int(num)
k = num_int
for i in range(1, num_int+1):
    sum = num_int * i
    print(num_int,"*",i,"=",sum)

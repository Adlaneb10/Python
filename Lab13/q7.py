string = input("Enter a string: ")


letters = [ch for ch in string if(ord(ch) >= ord('a') and ord(ch) <= ord('z') )]

if len(set(letters))==len(letters):
    print("This is a heterogram")

else:
    print("this is not a heterogram")

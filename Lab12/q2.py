def safe_input(promt,promt_type):
    if type(promt) == promt_type:
        return promt
    while True:
        try:
            convert = promt_type(promt)
        except ValueError:
            print(promt,"cant convert to",promt_type)
            promt = input("Enter a new promt")
        else:
            return convert

num = safe_input(input("pleaser enter a num:"),int)
float_p = safe_input(input("pleaser enter a float:"),float)
string = safe_input(input("pleaser enter a string:"),str)

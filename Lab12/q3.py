#Function that repeatedly
# prompts for file name

def prompt_open():
    runner = 0
    while runner == 0:
        file = input("Enter a file name: ")
        try:

            file = open(file, "r")
            print("first line", file=file)
            file.close()
            runner += 1
            
        except IOError:
            print("Invalid file name. Please try again")
        else:
            return file


prompt_open()

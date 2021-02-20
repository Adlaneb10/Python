import string

def mainmenu():
    options = 0
    runner = 0
    while runner == 0:
        print("\t\t\t MAIN MENU \t\t\t")
        options = input("1.search for docs\n2.Read Document\n3. Quit Program\n")

        if options == "1":
            menu1()
            runner = 0
        elif options == "2":
            menu2()
            runner += 1
        else:
            print("ERROR")

def menu1():
    doc = input("Enter document name: ")

def menu2():
    reader = input("Select which document")

mainmenu()

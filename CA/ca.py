# Program with built in search engine to search for key words and certain articles.
# Program can search for a document also to read a document as well.
# Author : Adlane Boulmelh (C19367031)
# Date 30/10/2020

import string

# Function for main menu this includes output to user to select menu options and also calls appropriate function when
# a specific key is selected.
def mainmenu():
    # variables that are used within def mainmenu()

    # Variable to help navigate through menu for user
    options = 0
    # Runner will help constantly display menu to user
    runner = 0
    # Will make sure user searches before reading a document
    checker_opt1 = 0

# while loop for menu
    while runner == 0:
# Display message to user and ask what they want to do

        print("Welcome\n What would you like to do?")
        options = input("1.Search for documents\n2. Read Document \n3. Quit Program\n")
        # if checker to check what user selected
        if options == "1":
            menu1()
            # to keep user in while loop and to keep displaying menu
            runner = 0
            # Checker to make sure user searches before reads
            checker_opt1 += 1
        # elif for option to read document
        elif options == "2":
            if checker_opt1 == 0:
                print("You must select option 1 first")

            else:
                menu2()
                runner += 1

        # menu option 3 to end program
        elif options == "3":
            menu3()
            runner += 1
            #exit
        # else for error checking for user
        else:
            print("ERROR: Invalid Entry. Please try again")
            runner = 0

# function for menu 1 to create dictionary and store each word in document in key corresponding to it's appropriate numbers
def menu1():
    # declare variables
    new_doc_check = 0
    word_tag = "document"
    dict_store = {}
    doc_find = ""

    # Open appropriate text document as "file"
    with open("ap_docs.txt","r")as file:
        # read in each line in text document in a for loop
        for line in file.readlines():
            # lower all characters in text document
            splitline_lower = line.lower()
            # splits each line in document using split function
            splitline_split = splitline_lower.split()
            # remove all unwanted punctuation for easy dictionary storage
            for word in splitline_split:
                new_words = word.strip(string.punctuation)
             # check for tag in list of words
                if word_tag in new_words:
                    new_doc_check += 1
                else:
                    dict_store[new_words] = new_doc_check

        doc_find = input("Enter the word related to desired document: ")
        # Error check if users entry cannot be found
        try:
            print("Documents fitting search: \n",dict_store[doc_find])

        except:
            print("This search query has not been found in document. Try again\n ")



    # print("This has been found in document",dict_store[doc_find])

# return variables such as dictionary for use in another function
    return dict_store
    return doc_find
    return doc_store

# Menu 2 will allow user to read a document they select
def menu2():
    set1 = set()
    # call returned variables for use in this function
    dict = menu1()

    word_search = menu1()

    doc_nums = menu1()

    each_doc = doc_reader()

# Tried to store what documents are related to search query
    for key,value in dict.items():
        if key == word_search:
            set1.add(value)

    doc_nums = int(input("Enter document number from 1-226: "))
    print(each_doc[doc_nums])

# Function that indicates program has ended
def menu3():
    print("Ending Program...")
    
    exit

# Function that stores all documents in a dictionary and document
# can be selected with given dictionary value and will then be printed
def doc_reader():
    #Varaibles
    word_tag = "<NEW DOCUMENT>"
    dict_docs = {}
    counter = 0

    # open file and read lines in file
    with open("ap_docs.txt","r")as file:
        for line in file.readlines():
            # if word tag is in line enter if and increment counter to keep
            # track of which document you are in
            if word_tag in line:
                counter += 1
            # else if word tag not in line then then add lines in to key until you reach a tag
            else:
                try:
                    dict_docs[counter] += line
                except:
                    dict_docs[counter] = line
# return dictionary to use in other function
    return dict_docs

mainmenu()

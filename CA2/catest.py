# Design an application to to manage a shopping cart.
# Design a shopping cart class in python - store basket as a dict
# Design a customer class with two sub classes Loyal customer and
# Bargain hunters. Each class should have an init and str
# each str method think of what info you will need to provide
# two methods of overload operators == add and radd
# implement command line menu in main func
# Author: Adlane Boulmelh C19367031
# Date: 05/12/2020

# import func that will get largest value in a dictionary
from heapq import nlargest
# import func that will get smallest value in a dictionary
from heapq import nsmallest


class ShopCart(object):
    """ Designed a class for a shopping cart which includes exclusive items and normal items diplay
    Also contains functions to add a product, remove a product, calculate total basket cost and display current basket"""
    def __init__(self, basket_list = [], exclusive_items = {}, normal_items = {}, total_bask = None):
        self.basket_list = basket_list
        self.exclusive_items = exclusive_items
        self.total_bask = total_bask
        self.normal_items = normal_items


        self.exclusive_items = {"ps5":500,"dior":120,"rolex":4000,"macbook":1000}
        self.normal_items = {"chicken":5,"eggs":2,"toast":1,"milk":2.5}

    def add_prod(self):
        # Function to add a product to your basket
        remove = 0
        print("Enter the product name you want to add to basket!")
        prod_name = str(input())

        # iterate through keys and values in dictionary
        for key,value in self.exclusive_items.items():
            # check if users entry is found and append
            if prod_name.lower() == key:
                self.basket_list.append(prod_name)
                self.basket_list.append(value)
                remove +=1

        for key,value in self.normal_items.items():
            # check if entry is in normal items dictionary and append
            if prod_name.lower() == key:
                self.basket_list.append(prod_name)
                self.basket_list.append(value)
                remove +=1

        # This will occur if users entry doesn't match/ does not exist
        if remove == 0:
            print("ERROR: Product you entered does not exist or is not available. Please try again")

        # IF users entry is found this will occur
        if remove >> 0:
            print("Successfully added", prod_name)

    def remove_prod(self):
        #Function to remove a product from a basket
        remove = 0
        print("Enter the product name you want to remove from ")
        prod_remove = str(input())

        # iterate through keys and values of exclusive items dict
        for key,value in self.exclusive_items.items():
            # if entry matches remove key and value from list
            if prod_remove.lower() == key:
                self.basket_list.remove(prod_remove)
                self.basket_list.remove(value)

                remove += 1
        for key,value in self.normal_items.items():
            # remove from list if entry matches
            if prod_remove.lower() == key:
                self.basket_list.remove(prod_remove)
                self.basket_list.remove(value)
                remove += 1

        # if entry is not found
        if remove == 0:
            print("ERROR: Product you entered does not exist in the basket. Please try again")
        # if entry is found and removed
        if remove >> 0:
            print("Successfully removed", prod_remove)

    def display_basket(self):
        # Function that will display the current basket to the user

        # if nothing is in basket and error will be displayed
        if self.basket_list == []:
            print("There is nothing in your basket. Try adding something...")
            return
        else:
            print("The items you have added to your basket are below.")
            print(self.basket_list)

    def calc_basket(self):
        # Function to calculate the total cost of the basket

        # variable names used in function
        temp_list = []
        address = ""
        happy_check = ""
        delivery_opt = 0
        # append items to a temp list
        for el in self.basket_list:
            if type(el) == int:
                temp_list.append(el)
        # sum list and store in total bask
        self.total_bask = sum(temp_list)
        # if nothing is in basket error will be displayed
        if self.total_bask == 0:
            print("You need to add something to your cart to checkout!")
            return
        # else a sum will be calculated
        if self.total_bask >> 0:

            print("The grand total is €", self.total_bask)

            # delivery option for customer
            print("Please select whether you want to do 1. Home delivery or 2. Click & Collect")
            # try user input
            try:
                delivery_opt = int(input())
                if delivery_opt not in [1,2]:
                    print("ERROR: Select 1 or 2")
            # if value error occurs print error message function
            except ValueError:
                error_print()

            # Home delivery option charge an extra fee
            if delivery_opt == 1:
                print("Thank you for selecting Home delivery.\n The cost is €5.99.")
                print("Please enter your address below.")
                # try get string input from user
                try:
                    address = str(input())
                # if value error print an error message
                except ValueError:
                    error_print()
                # Add delivery charge if delivery option selected
                self.total_bask += 5.99
                print("Thank you for your purchase of €",self.total_bask)
                print("Your delivery to {} will arrive in 3-5 working days.".format(address))
                exit()
            # if user wants to click and collect
            if delivery_opt == 2:
                print("Great! Are you happy with your items?")
                print("Enter Yes or No")
                try:
                    happy_check = str(input())
                except ValueError:
                    error_print()
                # Ask user what option for y or n for basket opinion
                if happy_check.lower().startswith("y"):
                    print("Thank you for your purchase of €{}\n Goodbye!".format(self.total_bask))
                    exit()
                if happy_check.lower().startswith("n"):
                    print("We will bring you back to the menu to change anything, if you wish!")
                    return
    # operator over load greatest item available
    def __gt__(self, other):
        """Printing the most expensive item available in normal items
        and exclusive items"""

        # use imported function from heapq import nlargest to find highest value in dict
        highest_excl = nlargest(1, self.exclusive_items, key = self.exclusive_items.get)
        highest_norm = nlargest(1, self.normal_items, key = self.normal_items.get)

        if highest_excl > highest_norm:
            print("\nMost expensive item is found in Exclusive items\n")
        else:
            print("\nMost expensive item is found in normal items\n")

    # operator over load cheapest item available
    def __lt__(self, other):
        """Printing which basket has the cheapest item between exclusive
        and normal items list"""

        # use imported function to find lowest values in dict from heapq import nlargest
        smallest_excl = nsmallest(1, self.exclusive_items, key = self.exclusive_items.get)
        smallest_norm = nsmallest(1, self.normal_items, key = self.normal_items.get)

        if smallest_excl < smallest_norm:
            print("\nCheapest item is found in Normal items\n")
        if smallest_norm < smallest_excl:
            print("\nCheapest item is found in Exclusive items\n")

    def __str__(self):
        return "Exclusive items available {}\n\nNormal items available {}".format(self.exclusive_items, self.normal_items)


class Customer(object):
    """ Customer class that will take in users first name and last name it includes the function cust_info"""
    def __init__(self,f_name = None,s_name = None):
        self.f_name = f_name
        self.s_name = s_name

    def cust_info(self):

        # ask user for their first name and second name
        print("Hi there please enter your first name!")
        f_name = input()
        print("Enter your second name.")
        s_name = input()
        print("Welcome {} {} !\n".format(f_name,s_name))

    def __str__(self):
        # string to print a welcome message
        result = "Welcome " + self.f_name +" " + self.s_name
        return result





class LoyalCust(Customer):
    """ Class for loyal customer to access the exclusive items"""
    def __init__(self, exclusive_prod = None):
        Customer.__init__(self,exclusive_prod)
        self.exclusive_prod = exclusive_prod
        self.exclusive_prod = {"PS5    ":"500","Dior   ":"120","Rolex  ":"4000","MacBook":"1000"}


    def list_types(self):
        # function which will list exclusive items in a pleasant manner
        print("Welcome Loyal customer please look at our exclusive items available for sale below\n")

        # print keys and values
        print("|Item|\t\t |PRICE|")
        for keys,values in self.exclusive_prod.items():
            print(keys,"\t €",values)

        return self.exclusive_prod



    def __str__(self):
        result = self.exclusive_prod
        return str(result)



class BargainCust(Customer):
    """ Class for bargain customer to display normal items"""
    def __init__(self,normal_prod = None):
        Customer.__init__(self,normal_prod)
        self.normal_prod = normal_prod
        self.normal_prod = {"Chicken":"5","Eggs   ":"2","Toast  ":"1","Milk   ":"2.5"}


    def list_types(self):
        # function to list normal items in a pleasant manner
        print("Welcome Bargain Hunter look at what we have available below\n")
        print("|Item|\t\t |PRICE|")
        # print keys and values
        for keys,values in self.normal_prod.items():
            print(keys,"\t €",values)



# function for main which will navigate through the program and menu
def main():
    # error preventative variables
    user_add = 0
    complete_check1 = 0
    add_remove_check = 0

    # print menu repeatedly after user completes a section each entry
    while True:
        print("--- Welcome to the Main-Menu ---\n\nPlease select an option below.\n"
          "1. Create a customer.\n2. List products.\n3. Add/remove a product "
          "to the shopping cart\n4. See current shopping cart\n5. Checkout")
        user_entry = input()
        while True:
            # error check
            try:
                user_entry = int(user_entry)
                if user_entry not in [1,2,3,4,5]:
                    error_print()
                break
            except ValueError:
                error_print()
                break
        # for first menu option
        if user_entry == 1:
            # Create a customer
            cust1 = Customer()
            cust1.cust_info()

            # error check variables
            complete_check1 += 1
            add_remove_check += 1

        # second menu option
        if user_entry == 2:
            # error check
            if complete_check1 == 0:
                print("ERROR: You must select option 1 first!")

            # if user selected option 1 proceed
            elif complete_check1 >> 0:
                cust_type = 0
                print("Select 1 if you are a Loyal Customer or 2 for a Bargain Hunter?")
                try:
                    cust_type = int(input())
                    if cust_type not in [1,2]:
                        print("ERROR: Invalid entry. Select 1 or 2")
                except ValueError:
                    error_print()
                # loyal customer
                if cust_type == 1:
                #List products available
                    first = LoyalCust(cust1)
                    first.list_types()

                # bargain customer
                if cust_type == 2:
                    second = BargainCust(cust1)
                    second.list_types()
        # menu option 3
        if user_entry == 3:

            if complete_check1 == 0:
                # Dont let user add/remove without making a customer
                print("ERROR: You must create a customer first!")
            if complete_check1 >> 0:

                print("Select 1 if you would like to add a product or 2 to remove a product?")
                try:
                    user_add = int(input())
                    if user_add not in [1,2]:
                        # Use function to print error message
                        error_print()
                except ValueError:
                    error_print()

                if user_add == 1:
                    ShopCart().add_prod()

                if user_add == 2:
                    ShopCart().remove_prod()

        # menu option 4
        if user_entry == 4:
            # Display shopping cart
            ShopCart().display_basket()
        # menu option 5
        if user_entry == 5:
            ShopCart().calc_basket()

def error_print():
    """Function to print error message instead of repeatedly"""
    print("ERROR: Invalid Entry!")


def test():
    """Testing functions with instances"""
    cust1 = Customer("Adlane","Boulmelh")
    cust2 = Customer("Y","Z")
    print(cust1)
    #sum =  + 5


    # operator overload of __gt__ ( greater than ) used
    shop1 = ShopCart([],{"PS5":500, "PS4":250}, {"Eggs":20},0)
    shop2 = ShopCart([],{"Rolex":700, "PS3":350}, {"Eggs":40},0)
    larger = shop1 > shop2

    # instance return __Str__ from ShopCart
    print(shop1)

    # operator overload of __lt__ ( less than ) used
    smaller = shop1 < shop2


# pre menu to select whether you would like to access test func or main menu func.
test_select = 0


while True:
    print("Would you like to access test function or normal menu function?")
    print("Select 1 for test and 2 for normal menu.")
    try:
        test_select = int(input())
        if test_select not in [1,2]:
            error_print()
    except ValueError:
        error_print()


    if test_select == 1:
        test()
    if test_select == 2:
        main()



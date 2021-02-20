# Design an application to to manage a shopping cart.
# Design a shopping cart class in python - store basket as a dict
# Design a customer class with two sub classes Loyal cust and
# Bargain hunters .Each class should have an init and str
# each str method think of what info you will need to provide
# two methods of overload operators == add and radd
# implement command line menu in main func
# Author: Adlane Boulmelh
# Date: 05/12/2020

class ShopCart(object):
    def __init__(self,basket_dict = {},product_dict = {},total_bask = None):
        self.basket_dict = basket_dict
        self.product_dict = product_dict
        self.total_bask = total_bask
        #basket_dict = {}
        # format of {"product name":"price"}
        product_dict = {"Chicken":"5","Eggs":"2","Toast":"1","Milk":"2.5"}
        print("Please select a product below\n", product_dict)

class Customer(object):
    def __init__(self, cust_status= 0):
        self.cust_status = cust_status


    def cust_info(self):
        print("Hi there please enter your first name!")
        f_name = input()
        print("Enter your second name.")
        s_name = input()
        print("Select 1 for a Loyal Customer or 2 for a Bargain Hunter")
        cust_status = int(input())
        # find out whether user is loyal or bargain hunter
        if cust_status == 1:
            cust_type = "Loyal"
        if cust_status == 2:
            cust_type = "Bargain Hunter"
        print("Welcome {} {} you are a {} customer!\n".format(f_name,s_name,cust_type))

    def __str__(self):
        return "String"
        #return None



class LoyalCust(Customer):
    def __init__(self, cust_status,exclusive_prod = None):
        Customer.__init__(self,cust_status,exclusive_prod)
        #cust_status_new = Customer(cust_status)
        self.exclusive_prod = exclusive_prod
        #cust_status_new = Customer(cust_status)
        #exclusive_prod = {"PS5":"500","Dior Perfume":"120","Rolex":"4000","Smart Water":"10"}
        #print("Loyal")

    def print_items(self):
        self.exclusive_prod = {"PS5":"500","Dior Perfume":"120","Rolex":"4000","Smart Water":"10"}
        print(self.exclusive_prod)

    def __str__(self):
        result = self.exclusive_prod
        return str(result)



class BargainCust(Customer):
    print("Bargain")
    pass


def main():

    while True:
        print("--- Welcome to the Main-Menu ---\n\nPlease select an option below.\n"
          "1. Create a customer.\n2. List products.\n3. Add/remove a product"
          "to the shopping cart\n4. See current shopping cart\n5. Checkout")
        user_entry = input()
        while True:
            try:
                user_entry = int(user_entry)
                if user_entry not in [1,2,3,4,5]:
                    continue
                break
            except ValueError:
                print("ERROR:Invalid entry!")
                break
        if user_entry == 1:
            # Create a customer
            cust1 = Customer()
            cust1.cust_info()

        if user_entry == 2:
            #Test if a number gets added to it
            #print(cust1.cust_status)
            #List products available

            if cust1.cust_status == 1:
            #    print(cust1.cust_status)
                loyal = LoyalCust(cust1)
                loyal.print_items()
            #    print(LoyalCust())



main()



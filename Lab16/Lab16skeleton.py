#!/usr/bin/python3

# Use the exchangeratesapi.io to perform currency conversions.
# https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD

import urllib.request
import string
import json
#create dict to store currency rates
#rates_EURGBP = json.loads('{"rates":{"GBP":0.8598},"base":"EUR","date":"2019-11-22"}')
#print(rates_EURGBP["rates"]["GBP"]) #0.8598
#print(rates_EURGBP["base"]) # EUR
#print(rates_EURGBP["date"]) # date printed
#rates_EURUSD = json.loads('{"rates":{"USD":1.1058},"base":"EUR","date":"2019-11-22"}')
#print(rates_EURUSD["rates"]["USD"])
#print(rates_EURUSD["base"])

class Currency:
    """Class currency used to convert exchange rate"""

    VALID_CURRENCIES = ['USD', 'EUR', 'GBP', 'AUD', 'CAD',
                        'CNY', 'ILS', 'MXN', 'RUB', 'THB', 'BRL']

    def __init__(self, amount=1, currency_type='USD'):
        # a quick way of checking for valid currencies
        # for a limited subset of valid currencies
        if currency_type in Currency.VALID_CURRENCIES:
            self.amount = amount
            self.currency_type = currency_type
        else:
            print("Invalid currency type: %s\n", currency_type)
            self.amount = 0
            self.currency_type = ''

    def convert_to(self, new_currency_type):
        if new_currency_type == self.currency_type:
            # nothing to do
            return Currency(self.amount, self.currency_type)

        if new_currency_type not in Currency.VALID_CURRENCIES \
                or self.currency_type not in Currency.VALID_CURRENCIES:
            print("Conversion from {} to {} not allowed".format(self.currency_type, new_currency_type))
            return

        # prepare URL
        url = "https://api.exchangeratesapi.io/latest?base="
        url += self.currency_type
        url += "&symbols=" + new_currency_type
        conv = urllib.request.urlopen(url)
        # read() returns an array of bytes, we want a string decoded in UTF-8
        response = conv.read().decode('UTF-8')
        #print (response)
        # 1 USD is €0.84
        #it is a JSON string use the package to manipulate the string
        response = json.loads(response)

        # Get info from json string and assign value to a var then do equation
        rate_val = response["rates"][new_currency_type]

        #Amount now contains conversion of USD to EURO
        amount = curr.amount * rate_val # or instead of curr.amount you can use
        #self.amount


        # Extract the exchange rate from the variable 'response' and finish the implementation of the method.
        # The return is given. Amount is the the correct converted amount that needs to be found


        print("{} {} => {} {}".format(self.amount, self.currency_type, amount, new_currency_type))
        return Currency(amount, new_currency_type)

    def __str__(self):
        return self.currency_type +" " + str(self.amount) + " new value"

    def __repr__(self):
        return (self.amount,self.currency_type)

    def __add__(self, other_curr):
        if type(other_curr) is int or type(other_curr) is float:
            new_amount = self.amount +other_curr
        elif type(other_curr) is Currency:
            if other_curr.currency_type != self.currency_type:
                other_curr = other_curr.convert_to(self.currency_type)
            x = self.convert_to(other_curr.currency_type)
            #print("xxx",x)
            new_amount = other_curr.amount + x.amount


            return Currency(new_amount,self.currency_type)
        else:
            print("Error invalid entry")

    def __sub__(self, other_curr):
        if type(other_curr) == Currency:
            subs = self.convert_to(other_curr.currency_type)
            new_amount = other_curr.amount - subs.amount

        return Currency(new_amount,self.currency_type)

    def __radd__(self, other_curr):
        return self.__add__(other_curr)


    def __rsub__(self, other_curr):
        new_curr = Currency(other_curr,self.currency_type)

        return new_curr - self

    def __gt__(self, other_curr):
        converted = self.convert_to(other_curr.currency_type)
        #Fix this problem occured
        if converted.amount > other_curr.amount:
            print("True")
        else:
            print("False")

# This main is incomplete because not all methods are tested
# Some outputs are given by the comments next to the commands. Your code should be able to output these when
# you remove the '#' in the beginning of the lines
#convert_to(5, "USD")
#print(x)


curr = Currency(1, "GBP")
#print(curr) # 7.50 USD
curr2 = Currency(1,"USD")
#print(curr2)  # 2.00 EUR
Currency.convert_to(curr,curr2.currency_type)

#add two currencies
sum = curr2 + curr
print(sum)

gt = curr > curr2


#Subtract two currencies include rsub
#sum_minus = 2 - curr2
#print(sum_minus)

#Using __radd__ method
#sum_radd = 5.2 + curr2
#print(sum_radd)

#Not working currently
#gt = curr2 >>  curr
#print(gt)

#new_curr = curr2.convert_to(curr.currency_type) # 2.000000 EUR => 2.211600 USD
#print(new_curr) # 2.21 USD
#sum_curr = curr + curr2 # 2.000000 EUR => 2.211600 USD
#print(sum_curr) # 9.71 USD
#sum_curr2 = curr + 5.5
#print(sum_curr2) # 13.00 USD

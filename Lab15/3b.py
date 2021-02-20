# Some information you might want
#in a bank account are the IBAN, account number,
# available funds, a list with the last
#5 transactions. You might also add methods to withdraw and deposit money
class BankAccount(object):
    def __init__(self, iban= " ", acc_num= 0, bal= 0, trans = None ):
        self.new_iban = iban
        self.acc = acc_num
        self.balance = bal
        self.trans_dict = trans
    def withdraw(self,new_bal):
        amount = 500
        self.balance = self.balance - amount
        print("\nWithdrawal\nYou withdrew €",amount)
        print("New balance is €",self.balance)
        self.trans_dict = amount

        return amount

    def deposit(self,new_bal2):
        amount = 10000
        self.balance = self.balance + amount
        print("\nDeposit\nYou made a deposit of €",amount)
        print("Your new balance is €",self.balance)
        return amount



    def __str__(self):
        return "IBAN: " + self.new_iban + "\nAccount Number: " + str(self.acc) + "\nBalance: " + str(self.balance) + "\nTransactions: " + str(self.trans_dict)

class MinBank(BankAccount):
    def __init__(self, iban= " ", acc_num= 0, bal= 0, trans = None, min_threshold = 100):
        MinBank.__init__(self, iban,acc_num,bal,trans,min_threshold)
        self.min = min
    def withdraw(self,new_bal):
        pass
acc1 = BankAccount("IE123",456789,4500,[])
print(acc1)

acc1.withdraw(500)
#print(acc1)

acc1.deposit(10000)
#print(acc1)

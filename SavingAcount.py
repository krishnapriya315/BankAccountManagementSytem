# referance  class defined oin another module /file

from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def dummymetod(self):

        print("this is a dummymethod")

    
    def calculate_interest(self):
        interest=(self.get_balance()) *5/100
        return interest

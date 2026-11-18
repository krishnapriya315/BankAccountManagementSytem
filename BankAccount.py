from abc import ABC, abstractmethod


# creating a 

class BankAccount(ABC):

# constructor of the class 
    def __init__(self):
         self.__account_balance=0       #a private variable -encaplution 

# this method must be inheried by chile classes

    @abstractmethod
    def calculate_interest():
        pass

    def display_balance(self):
        print(f'the accunt balance is : {self.__account_balance}')



    def get_balance(self):
        return self.__account_balance
     


    def deposit_amount(self,amount):
        if amount>=0:
            self.__account_balance = self.__account_balance + amount
            print('amount added to balance')
        else:
            print('Please enter a positive number as deposit amount')

    
    def withdraw_amount(self,amount):
        if ( (amount > 0 ) and ( amount <= self.__account_balance) ):
            self.__account_balance = self.__account_balance - amount
            print('Balance ads been updated')
        elif( amount > self.__account_balance) :
            print('Insufficient fund')
        else :
            print('Please enter a positive number as withdrawal amount')





    


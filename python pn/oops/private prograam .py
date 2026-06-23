class bankaccount:
    def __init__(self , name , balance , pin ):
      self.name = name #public
      self._balance = balance #protected
      self.__pin = pin #private
    #public method
    def show_details(self):
        print("name :" , self.name)
        print("balance :" , self._balance)
    #private methd
    def __show_pin(self):
        print("pin :" , self.__pin)
    #public method to acces private method     
    def access_pin(self):
        self.__show_pin()       

#child class
class atm(bankaccount):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("amount withdraw success")
            print("remaining balance", self._balance)     
        else:
            print("insufficient balance")
# object creation
# first objectr of bankaccount
a = atm("rahul" , 5000 , 1234) 
a.show_details()   
a.withdraw(1000)             
a.access_pin()
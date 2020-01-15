import json
from EX06_G.customer import Customer
from EX06_G.account import Account
class jsondriver:
   def __init__(self):
       self.__data=None

   def show(self):
      return (self.__data)

   def get_data(self):
       return (self.__data)


   def read(self,fname):
       with open(fname, encoding="utf-8") as f:
           self.__data =json.load(f)
           print("*"*20,"使用customer convert_to_customers","*"*20)

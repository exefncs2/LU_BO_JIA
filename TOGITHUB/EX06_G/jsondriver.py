import json
from EX06_G.customer import Customer
from EX06_G.account import Account
class jsondriver:
    def __init__(self,data=None):
        self.data=data

    def show(self):
        for k,v in self.data:
            print(k,"\t",v)

    def get_data(self):
        if self.data !=None:
            return tuple(self.__data)
        else:return self.data
    def read(self):
        with open("customer.json", encoding="utf-8") as f:
            x = json.load(f)
            # print(x)
            # self.convert(x)
            print("*"*20,"使用customer convert_to_customers","*"*20)
            Customer.convert_to_customers(x)
            print("*" * 20, "使用x.items()", "*" * 20)
            for k, v in x.items():
                print(k, "\t", v)
    def read2(self):
        with open("account.json", encoding="utf-8") as f:
            x = json.load(f)
            print("*"*20,"使用convert_to_account","*"*20)
            Account.convert_to_accounts(x)
            print("*" * 20, "使用x.items()", "*" * 20)
            for k, v in x.items():
                print(k, "\t", v)
    # @staticmethod
    # def convert(x):
    #     data = []
    #     for a in x:
    #         data.append(a)
    #     return jsondriver(data)



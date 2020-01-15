from EX04_F.account import Account
from EX04_F.bank import bank
from EX04_F.customer import Customer, A

class P:
    def __init__(self):
        self.stranyting=""
        self.intanyting=0
    def show(self):
        print(self.stranyting)
        print(self.intanyting)

c = Customer()
a =Account()#wirle 3 acc cust balance
b =bank()
p=P()
#c.test=p
print("@@@@@@@@CUSTOMER@@@@@@@@@@@@@@")
c.read()#直接輸出記憶體位置
c.add_account("N")
c.show()

print("------------ACCOUNT-----------------")
a.read()
a.show()
print("************BANK*****************")



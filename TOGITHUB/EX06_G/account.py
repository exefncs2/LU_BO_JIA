class Account:
   def __init__(self,acc_id,cust_id,balance):
       self.acc_id=acc_id
       self.cust_id=cust_id
       self.balance=balance

   def show(self):
       print("acc_id:",self.acc_id)
       print("cust_id:", self.cust_id)
       print("balance:", self.balance)

   @staticmethod
   def convert_todict_account(x2):#把格式符合的資料轉成dict
       return Account(x2["acc_id"], x2["cust_id"], x2["balance"])


   @staticmethod
   def convert_to_accounts(xx):
       a=[]
       for n in xx:
           acc = Account.convert_todict_account(n)
           a.append(acc)
       return a
from EX06_G.account import Account
class Customer:
   def __init__(self, id, name, A):
       self.id = id
       self.name = name
       self.accounts = A

   def show(self):
       print(self.__dict__)
       print("--------客戶資訊---------")
       print("ID=",self.id)
       print("name=",self.name)
       print("accounts=")
       for n in self.accounts:
           print("-------帳戶資訊----------")
           #----------------未處理 型態轉換成dict-------------------------------
           Account.convert_todict_account(n).show()
           #---------------處理好資料 型態dict---------------------
           # n.show()

   def add_account(self, x):
       self.accounts.append(x)
   @staticmethod
   def convert_to_customers(x):
       acc=[]
       ID = x["cust_id"]
       name = x["name"]
       #------------acc方法轉呈字串送出
       for k in x["accounts"]:
           acc.append(k)
       return Customer(ID, name,acc)
       #-------------送出已處理好資料
       # xxx=x["accounts"]
       # account= Account.convert_to_accounts(xxx)
       # return Customer(ID, name,account)
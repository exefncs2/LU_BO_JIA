import csv
class Account:
    def __init__(self,acc_id=0,cust_id=0,balance=0):
        self.acc_id=acc_id
        self.cust_id=cust_id
        self.balance=balance

    def show(self):
        print("accid:",self.acc_id)
        print("custid:", self.cust_id)
        print("balance:", self.balance)

    def read(self):
        a = []
        with open('Accounts.csv', newline="", encoding='utf-8')as f:
            csv_reader = csv.reader(f, delimiter=" ")

            for x in csv_reader:
                C = self.convert_to_account(x)
                a.append(C)
                C.show()

    @staticmethod
    def convert_to_account(x):
        acc_id=int(x[0])
        cust_id=int(x[1])
        balance=int(x[2])
        return Account(acc_id,cust_id,balance)
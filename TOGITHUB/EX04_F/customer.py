import csv
A=[]
class Customer:
    def __init__(self,id=0, name=""):
        self.id=id
        self.name=name
        self.accounts=[]
        self.test=""
    def show(self):
       print(self.id)
       print(self.name)
       # for s in self.accounts:
       #      s.show()
    def add_account(self,x):
        self.accounts.append(x)
    def read(self):
        self.accounts = []
        with open('Customers.csv', newline="", encoding='utf-8')as f:
            csv_reader = csv.reader(f, delimiter=" ")
            for x in csv_reader:
                c=self.convert_to_customers(x)
                self.accounts.append(c)
                c.show() #輸出記憶體位置
                A.append(c)

    @staticmethod
    def convert_to_customers(x):
        ID = int(x[0])
        Name = x[1]

        return Customer(ID, Name)

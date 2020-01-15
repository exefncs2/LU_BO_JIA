class bank:
    def __init__(self):
        self.name=""
        self.customers=[]

    def add_customer(self,c):
        self.customers.append(c)

    def show(self):
        print("name:"+self.name+"\n  customers:"+str(self.customers))
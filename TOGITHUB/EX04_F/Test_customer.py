import csv

from EX04_F.customer import Customer

customer=[]
with open("Customers.csv",newline='',encoding='utf-8')as f:
    csv_reader=csv.reader(f,delimiter=" ")
    for x in csv_reader:
        c=Customer.convert_to_customers(x)
        customer.append(c)
    for x in customer:
        x.show()
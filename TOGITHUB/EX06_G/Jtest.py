from EX06_G.customer import Customer
from EX06_G.json剖析器 import jsondriver

j=jsondriver()
j.read("customer.json")
j.show()
print("*"*120)
data=j.get_data()
c=Customer.convert_to_customers(data)
c.show()

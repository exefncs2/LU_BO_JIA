from EX05_F.CSVdriver import csvdriver

csv_Driver=csvdriver()
csv_Driver.read(filename="test01",maker=",").show()
c_data=csv_Driver.get_data()
print("/"*30)
print(c_data)

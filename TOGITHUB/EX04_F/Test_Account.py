import csv

from EX04_F.account import Account

accounts=[]
with open("Accounts.csv",newline='',encoding='utf-8')as f:
    csv_reader=csv.reader(f,delimiter=" ")
    for x in csv_reader:
        c=Account.convert_to_account(x)
        accounts.append(c)
    for x in accounts:
        x.show()
import csv
a=[]
import student
with open('D:\PYSON TEST\TYPE_A\TYPEF\student.csv',newline="",encoding='utf-8')as f:
     csv_reader=csv.reader(f,delimiter=",")
     for x in csv_reader:
        print(x)
        st=student.student.convent_to_student(x)
        a.append(st)
#C:/Users/ASUS/Desktop/TYPE_A/
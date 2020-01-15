import csv
from TYPEF import test_read

with open('student.csv','w',encoding='utf-8') as f:
    csv_writer=csv.writer(f,delimiter="\n")
    for wt in test_read.a:
        csv_writer.writerow([wt.name,wt.eng,wt.math])
print("file is over")

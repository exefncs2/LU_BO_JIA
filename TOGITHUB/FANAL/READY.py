from faker import Faker
import random as rd
import pandas as pd

names=[]
eng=[]
math=[]
for n in range(10):
    F1=Faker().first_name()
    F2=Faker().last_name()
    eng.append(rd.randint(50,100))
    math.append(rd.randint(50, 100))
    # print("{:<1} {:^10} {:^1} {:>4}".format(F1,F2,eng,math))
    names.append(F1+" "+F2)
    s = {"name": names, "eng": eng, "math": math}
df = pd.DataFrame(s)
print(df)
#更改地10行
i=df.last_valid_index()+1
print("i=",i)
df.loc[i]=["fucker",69,69]
# print(df)
#(第10(i)行,符合索引值的,更改數值)系統會不建議使用
# df.set_value(i,"eng",100)
# print(df)
#增加欄位
print("--------------------加入total,class--------------------------------")
df["total"]=df["eng"]+df["math"]
a=[]
c=["A班","B班"]
for T in range(i+1):
    a.append(rd.choice(c))
    #隨機選取()內數值
print(a)
s=pd.Series(a)
#DataFrame跟Series一樣，可以指定index，但這邊可以想像成DataFrame是多個Series組成。
df["class"]=s

print(df)
print("--------------------分組--------------------------------")
g=df.groupby(by="class")
print(type(g))
df_mean=g["eng","math"].mean()
print(df_mean)
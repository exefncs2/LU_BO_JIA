import pandas as pd
gdp=pd.read_csv("D:\PYSON TEST\TYPE_A\TYPEI\gdp.csv")

print("---------------------------------------------------------")
AG=gdp.groupby(by="country")#by=可不加
G=AG["pop","lifeExp","gdpPercap"]
MEAN=G.mean()
print("---------------mean-----------------------")
print(MEAN)
MAX=G.max()
print("----------------max----------------------")
print(MAX)
MIN=G.min()
print("------------------min--------------------")
print(MIN)
Q2=G.quantile(q=0.5)#無輸入q預設0.5
print("-----------------q2---------------------")
print(Q2)
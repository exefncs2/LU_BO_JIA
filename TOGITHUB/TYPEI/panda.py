import pandas as pd
df=pd.read_csv("D:\PYSON TEST\TYPE_A\TYPEI\gdp.csv")
print(df)
print(type(df))
print("-------------copy---------------------------")
df2=df.copy()
print(df2)
print("----------------head------------------------")
df3=df.head(n=3)
print(df3)
print("----------------tall------------------------")
df4=df.tail(n=3)
print(df4)
print("------------------info----------------------")
df.info()
print("----------------describe------------------------")
df5=df.describe()
print(df5)
print("----------------shape------------------------")
print(df.shape)
列數,欄數=df.shape
print("列數",列數,"欄數",欄數)
print("----------------columns------------------------")
print(df.columns)
for 欄名 in df.columns:
    print(欄名)
print("----------------index------------------------")
print(df.index)
for i in df.index:
    print(i)
print("------------------sort----------------------")
df6=df.sort_values(by=["gdpPercap"])
print(df6)
print("------------------series----------------------")
s1=df["gdpPercap"]>1000
print(type(s1))
print("s1序列資料: ")
print(s1)
df7=df[s1]
print("-----------------origin-----------------------")
print(df)
print("------------------df7-------------------------")
print(df7)
print("------------------s2-------------------------")
s2=df["gdpPercap"]
print(s2)
print("----------------排序---------------------------")
s3=s2.sort_values(ascending=True)
print(s3)




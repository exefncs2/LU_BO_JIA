import pandas as pd
gdp=pd.read_csv("D:\PYSON TEST\TYPE_A\TYPEI\gdp.csv")
s1=gdp["continent"]=="Asia"
s2=gdp[s1].sort_values(by="lifeExp",ascending=True)
print(s2["lifeExp"])
print("---------------------------------------------------------")
s3=(gdp["year"] <=2007) &  (gdp["year"] >=2000)
s4=gdp[s3]
s5=s4["gdpPercap"].mean()
print(s5)
print("---------------------------------------------------------")
s6=gdp["country"]
#------取得所有國家名(不重複)--------
s7=[]
for n in s6.values:
    if not n in s7:
            s7.append(n)
#-------國家名對上計算個資料---------------------
for i in range(len(s7)):
    s8=gdp[gdp["country"]==s7[i]]# 整體（ Ture 只有對到的)
    s9=s8["gdpPercap"]
    print(s7[i])#第[i]次執行中只有一個國家名會對到
    s9_min=s9.min()
    print("min=",s9_min)
    s9_Q1=s9.quantile(q=0.25)
    print("Q1=",s9_Q1)
    s9_Q2=s9.quantile(q=0.5)
    print("Q2=",s9_Q2)
    s9_Q3=s9.quantile(q=0.75)
    print("Q3=",s9_Q3)
    s9_max=s9.max()
    print("max=",s9_max)



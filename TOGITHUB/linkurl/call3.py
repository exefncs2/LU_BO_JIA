import requests
r=requests.get("http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-001889-001")
print(r.status_code)
r.encoding="utf-8"
#data=r.text
data=r.json()

for j in data:
    print(j)
# 目標為json使用
#print(data)
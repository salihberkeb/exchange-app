import json

import requests

url = "https://api.apilayer.com/exchangerates_data/latest?symbols="

payload = {}
headers= {
  "apikey": ""
}
print("-----------------------WELCOME TO CURRENCY CALCULATOR-----------------------\n")
bozulan_doviz=input("bozulan döviz türü: ")
alinan_doviz=input("\nalınan döviz türü: ")
miktar=input(f"\nNe kadar {bozulan_doviz} bozdurmak istiyorsun?: ")

response = requests.request("GET", url+alinan_doviz+"&base="+bozulan_doviz, headers=headers, data = payload)

status_code = response.status_code
result =json.loads(response.text)


print("1 {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],[alinan_doviz]))

print("{0}{1}={2}{3}".format(miktar,bozulan_doviz,float(miktar)*float(result["rates"][alinan_doviz]),[alinan_doviz]))


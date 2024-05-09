import pandas as pd
import requests
from bs4 import BeautifulSoup

# for i in range (2,10):
#     url="https://www.flipkart.com/search?q=iphone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_6_3_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_3_na_na_na&as-pos=6&as-type=RECENT&suggestionId=iphone&requestId=dd8ccfb5-402f-4c6a-8b56-1e5a18ab8273&as-searchtext=ipo"+str(1)
#     r=requests.get(url)
#     print(r)
#     soup=BeautifulSoup(r.text,"lxml")
# # print(soup)

#     np=soup.find("a",class_="cn++Ap").get("href")
#     #print(np)
#     li="https://www.flipkart.com"+np
#     print(li)

#     url=li
#     r=requests.get(url)
#     soup=BeautifulSoup(r.text,"lxml")
    
product_name=[]
prices=[]
Desc=[]
review=[]

for i in range (2,20):
    url="https://www.flipkart.com/search?q=iphone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_6_3_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_3_na_na_na&as-pos=6&as-type=RECENT&suggestionId=iphone&requestId=dd8ccfb5-402f-4c6a-8b56-1e5a18ab8273&as-searchtext=ipo"+str(i)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    names=soup.find_all("div",class_="KzDlHZ")
    box=soup.find("div",class_="DOjaWF gdgoEp")
#print(names)
    for i in names:
      name=i.text
      product_name.append(name)
   
#print(product_name)
#print(len(product_name))

    names_1=box.find_all("div",class_="Nx9bqj _4b5DiR")
    for i in names_1:
      names_1=i.text
      prices.append(names_1)
#print(prices)
#print(len(prices))

    names_2=box.find_all("ul",class_="G4BRas")
    for i in names_2:
     names_2=i.text
     Desc.append(names_2)
#print(Desc)

    names_3=box.find_all("div",class_="XQDdHH")
    for i in names_3:
        names_3=i.text
        review.append(names_3)
#print(review)
#print(len(review))

# pr_nm=[]
# for i in range(len(product_name)):
#      pr_nm.append(product_name[i])
#      pr_nm.append(prices[i])
    
# print(pr_nm[1])


df=pd.DataFrame({"Product Name":product_name,"Prices":prices,"Description":Desc,"Reiew":review})
print(df)
 
df.to_csv("E:/Download/Interview data/Flipkart/Flipkartphonesunder50000.csv")

    # Append elements from both lists alternately

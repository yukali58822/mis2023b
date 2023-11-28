import requests
from bs4 import BeautifulSoup

url = "https://www1.pu.edu.tw/~tcyang/course.html"
Data = requests.get(url)
Data.encoding = "utf-8"
# print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")

results = sp.select(".team-box") #取多筆
Result = ''
for result in results:
    Result += "<a href="+ result.find('a').get('href')+ ">" + result.text +"</a><br>"
    Result += result.find('a').get('href') +"<br>" +"<br>" #取一筆




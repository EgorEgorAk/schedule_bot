import requests
from bs4 import BeautifulSoup

GROUP_ID="56043"
date="2024-12-02"
URL="https://www.sut.ru/studentu/raspisanie/raspisanie-zanyatiy-studentov-ochnoy-i-vecherney-form-obucheniya"



result = requests.get(URL, params={ "group": GROUP_ID, "date": date}, 
                      headers={
                          "User-Agent": 
                               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
                           }
                    )
html = result.text
with open("raspisanie.html", "w") as f:
    f.write(html)

soup = BeautifulSoup(html, "html.parser")

for element in soup.find_all("span", {"class": "teacher"}):
    print(element.text, element.get("title", None))
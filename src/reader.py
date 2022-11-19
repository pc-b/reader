import json
import requests
from bs4 import BeautifulSoup



# m ake chapte getter
def getChapter(num):
    url = "https://light-novelpub.com/lightnovelpub/the-beginning-after-the-end/chapter-" + num
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.find(id="chr-content")
    print(text.text)



# lol Found the hack
base = "https://light-novelpub.com/ajax/chapter-archive?novelId="


url = "https://light-novelpub.com/ajax/chapter-archive?novelId=the-beginning-after-the-end"


testUrl = "https://light-novelpub.com/lightnovelpub/the-beginning-after-the-end/"


page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")

chapContainer = soup.find("div", class_="panel-body")

for row in chapContainer:
    if row != "\n":
        for col in row:
            if col != "\n":
                for li in col.contents[1]:
                    if li != "\n":
                        print(li.text.strip())


num = input("Enter chapter number to retrieve: ")

getChapter(num)



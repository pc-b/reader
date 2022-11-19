import requests
import json
from bs4 import BeautifulSoup




# set up link
base = "https://light-novelpub.com/lightnovelpub/"
title = input("Enter name of novel: ")
url = base + title.replace(" ", "-").lower()

# get page w requests
page = requests.get(url)


# get w bs4
soup = BeautifulSoup(page.content, "html.parser")







#  get author
meta = soup.find("ul", class_="info info-meta")
author = ""
for li in meta:
    if li != "\n" and li.contents[1].text == "Author:":
        author = li.contents[3].text


# get genre
genres = ""
for li in meta:
    if li != "\n" and li.contents[1].text == "Genre:":
        for genre in li:
            if genre != "\n" and genre.text != "Genre:":
                genres += genre.text.strip()
        


# get status
status = ""
for li in meta:
    if li != "\n" and li.contents[1].text == "Status:":
        status = li.contents[3].text


#get description




# get total number of chapters on this site...
chapters = soup.find("div", class_="l-chapter")
chapterNum = ""
text = chapters.text
index = text.find("Chapter")
newLineIndex = text[index:].find("\n")
text = text[index:newLineIndex+index]
chaps = text[8:]
chaps = [x for x in chaps if x.isdigit()]
for x in chaps:
    chapterNum += x
print(chapterNum)




# The beginning after the end


out_file = open("myfile.json", "w")


Dictionary = {"Title":title, "Author":author, "Genre":genres, "Status":status, "Chapters":chapterNum}

jform = json.dumps(Dictionary, skipkeys = True, allow_nan = True, indent = 6)



out_file.write(jform)
out_file.close()
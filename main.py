import requests
import json
from bs4 import BeautifulSoup

url = "https://qiita.com/"
webhook_url = "https://hooks.slack.com/services/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"

html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

text = ""

items1 = soup.find_all(class_="css-qrra2n")[:5]
items2 = soup.find_all(class_="css-vvapww")[:5]
items3 = soup.find_all("footer")[:5]

for i in range(5):
    text += "Title："
    text += items1[i].get_text()
    text += "\nURL："
    text += items1[i].get("href")
    text += "\nCategory："
    for j in items2[i].find_all(class_="css-4czcte"):
        text += j.get_text()
        text += "  "
    text += "\nLikes："
    text += items3[i].find(class_="css-70qvj9").find(class_="css-1laxd2k").get_text()
    text += "\n\n"

requests.post(webhook_url, data=json.dumps({
    "text": text
}))

import pyttsx3
import requests


def talk(command):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.say(command)
    engine.runAndWait()

news = requests.get("https://inshorts.me/news/top?offset=0&limit=5")
data = news.json()
newsnum = 0
while data:
    newsnum = newsnum+1
    title = data['data']['articles'][newsnum]['content']
    print(title)
    talk(title)
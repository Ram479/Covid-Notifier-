import requests
import time
from bs4 import BeautifulSoup
page = requests.get("https://www.worldometers.info/coronavirus/country/india/")
soup = BeautifulSoup(page.content, 'html.parser')
value=soup.find_all( class_="maincounter-number")
p=value[0].get_text()
p=p.strip("\n")
p1=value[1].get_text()
p1=p1.strip("\n")
p2=value[2].get_text()
p2=p2.strip("\n")
title="COVID-19 Alert"
message=f"Till now, there are {p}active cases in india in which {p1} has been reported dead and {p2} has been recovered so far... So please stay home and stay safe.. "
from plyer import notification
if __name__=="__main__":
    for i in range(2):
        notification.notify(
        title=title,
        message=message,
        timeout=10)
    time.sleep(8)
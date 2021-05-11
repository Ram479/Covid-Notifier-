import requests
import time
from bs4 import BeautifulSoup
page=requests.get("https://www.worldometers.info/coronavirus/country/india/")
soup=BeautifulSoup(page.content,'html.parser')
value=soup.find_all(class_="maincounter-number")
p=value[0].get_text()
p=p.strip("\n")
p1=value[1].get_text()
p1=p1.strip("\n")
p2=value[2].get_text()
p2=p2.strip("\n")
msg=f'Total No of active cases in india is {p} out of which {p1} has been reported dead and {p2} has been recovered so far...'
titl='Covid-19 Alert'
from plyer import notification
if __name__ == "__main__":
    for i in range(3):
    
        notification.notify(
            title=titl,
            message=msg,
            timeout=10
        )
    time.sleep(6)
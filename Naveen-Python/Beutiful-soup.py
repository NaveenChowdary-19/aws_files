from bs4 import BeautifulSoup
import requests
with open('Portfolio-Website/GmailMob.html') as html_file:
    soup=BeautifulSoup(html_file,'html5lib')
    
for htags in soup.find("div",class_="col-12"):
    print()
#match = soup.find("h3")
#print(match.text)
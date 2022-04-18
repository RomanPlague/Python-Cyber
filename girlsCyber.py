from bs4 import BeautifulSoup as bs
import urllib.request as re
import requests
import sys
if len(sys.argv)!=2:
        print("Usage:\npython girlsCyber.py UID")
        exit()
print("Loading...")
urls=["https://assess.girlsgocyberstart.org/challenge-files/clock-pt1?verify="+str(sys.argv[1]),
"https://assess.girlsgocyberstart.org/challenge-files/clock-pt2?verify="+str(sys.argv[1]),
"https://assess.girlsgocyberstart.org/challenge-files/clock-pt3?verify="+str(sys.argv[1]),
"https://assess.girlsgocyberstart.org/challenge-files/clock-pt4?verify="+str(sys.argv[1]),
"https://assess.girlsgocyberstart.org/challenge-files/clock-pt5?verify="+str(sys.argv[1])]
girlsFlag=""
for a in urls:
	page=re.urlopen(a)
	soup=bs(page,"html.parser")
	girlsFlag=girlsFlag+str(soup)
print(girlsFlag)
url="https://assess.girlsgocyberstart.org/challenge-files/get-flag?verify="+str(sys.argv[1])+"&string="+str(girlsFlag)
r=requests.get(url=url)
print("get",r.text)
r=requests.post(url=url)
print("post",r.text)
#8xGy%2FZzL4eK9xG%2FFAPie1Q%3D%3D

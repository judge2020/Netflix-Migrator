import http.cookiejar as cookiejar
import requests, datetime, json, os
from bs4 import BeautifulSoup

cj = cookiejar.MozillaCookieJar('cookies.txt')
cj.load()

req = requests.get('https://www.netflix.com/viewingactivity', cookies=cj)

if'class="profile-selector"' not in req.text:
    print('Cookies.txt invalid. Please see readme.md')
    os._exit(1)
jar = BeautifulSoup(req.text, 'html.parser')

elements = jar.find_all('a')
titles = []
for ele in elements:
    title = ele.get('href')
    if "/title" not in str(title):
        continue
    titles.append(str(title.replace('/title/', '')))

profileName = str(jar.find("img", {"class": "avatar"}).get('alt'))
print('Dumping profile ' + profileName)
# Title list is in order of most recent, so reverse it
titles.reverse()


time = datetime.datetime.now().strftime("%I.%M%p_%m_%d_%Y")

with open('titles_' + profileName + '_' + time + '.txt', 'w') as outfile:
    json.dump(titles, outfile)
from bs4 import BeautifulSoup
import requests

url = "http://www.homes.com/"

querystring = {"uri":"property/3501-lafayette-blvd-norfolk-va-23513/id-400028660479/"}


response = requests.request("GET", url, params=querystring)

#print(response.text)

soup = BeautifulSoup(response.text)

print(soup)
# images = soup.find_all('a')
# print(images)

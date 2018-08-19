#import webbrowser
#import sys
import requests
import bs4
#from bs4 import BeautifulSoup


#The tide information is parsed from the website:
#https://www.tide-forecast.com/locations/Carlsbad/tides/latest
#I do not accept responsibility for any amendments or changes to the data whilst it is displplayed.
#it is the user's responsibility to ensure that their hardware is configured to display the information as intended.
# We do not accept responsibility for any changes or representations of our data made by third parties or syndicates.



url = "https://www.tide-forecast.com/locations/Carlsbad/tides/latest"
res = requests.get(url)
#res.raise_for_status()

#Parse website
parse = bs4.BeautifulSoup(res.text)
#type(parse)
#parse.soup.select()

tide = parse.findAll('td', {'class':'time tide'})

high = tide[3].text
low = tide[4].text

#Below is commented out to test.
#print(tide)
#print(high)
#print(low)


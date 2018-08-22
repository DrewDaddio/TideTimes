import requests
import bs4
import html2text


#The tide information is parsed from the website:
#https://www.tide-forecast.com/locations/Carlsbad/tides/latest
#I do not accept responsibility for any amendments or changes to the data whilst it is displplayed.
#it is the user's responsibility to ensure that their hardware is configured to display the information as intended.
# We do not accept responsibility for any changes or representations of our data made by third parties or syndicates.

url = 'https://www.tideschart.com/United-States/California/San-Diego-County/Carlsbad/'

def get_text():
    res = requests.get(url)
    return res.text

res = get_text()

parse = bs4.BeautifulSoup(res)
#print(parse)
#type(parse)
#print(parse)
#parse.soup.select()

tide = parse.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

#Below is commented out to test.
#print(tide)
tide0 = tide[0].text
tide1 = tide[1].text
highlow = tide0 + '. ' + tide1 + '.'
highlow = html2text.html2text(highlow)

print(html2text.html2text(highlow))

#print(tide0)
#print(tide1)
#print(tide)
#print(tide0)
#print(tide1)
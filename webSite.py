import requests
import bs4
import html2text

beaches = {}

#I do not accept responsibility for any amendments or changes to the data whilst it is displplayed.
#it is the user's responsibility to ensure that their hardware is configured to display the information as intended.
# We do not accept responsibility for any changes or representations of our data made by third parties or syndicates.

url = 'https://www.tideschart.com/United-States/California/San-Diego-County/Carlsbad/'

def get_text():
    res = requests.get(url)
    return res.text

res = get_text()

parse = bs4.BeautifulSoup(res)

tide = parse.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

tide0 = tide[0].text
tide1 = tide[1].text
highlow = tide0 + '. ' + tide1 + '.'
highlow = html2text.html2text(highlow)
carlsbadCA = "Carlsbad, CA tide times - "

beaches[highlow] = (carlsbadCA)

#print(html2text.html2text(highlow))

#Venice Beach
venice = 'https://www.tideschart.com/United-States/California/Los-Angeles-County/Venice-City-Beach/'
def get_text1():
    res = requests.get(venice)
    return res.text

venice = get_text1()

venice = bs4.BeautifulSoup(venice)

venice = venice.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

venice0 = venice[0].text
venice1 = venice[1].text
venice = venice0 + '. ' + venice1 + '.'
venice = html2text.html2text(venice)
#print(venice)

veniceCA = "Venice Beach, CA tide times - "
beaches[venice] = veniceCA

#San Francisco
sanFran = 'https://www.tideschart.com/United-States/California/San-Francisco/'
def get_text1():
    res = requests.get(sanFran)
    return res.text

sanFran = get_text1()

sanFran = bs4.BeautifulSoup(sanFran)

sanFran = sanFran.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

sanFran0 = sanFran[0].text
sanFran1 = sanFran[1].text
sanFran = sanFran0 + '. ' + sanFran1 + '.'
sanFran = html2text.html2text(sanFran)

sanFranCA = "San Francisco, CA tide times - "
beaches[sanFran] = sanFranCA


#Monterey
monterey = 'https://www.tideschart.com/United-States/California/Monterey/'
def get_text1():
    res = requests.get(monterey)
    return res.text

monterey = get_text1()

monterey = bs4.BeautifulSoup(monterey)

monterey = monterey.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

monterey0 = monterey[0].text
monterey1 = monterey[1].text
monterey = monterey0 + '. ' + monterey1 + '.'
monterey = html2text.html2text(monterey)

montereyCA = "Monterey, CA tide times - "
beaches[monterey] = montereyCA

#Santa Cruz
santaCruz = 'https://www.tideschart.com/United-States/California/Santa-Cruz/'
def get_text1():
    res = requests.get(santaCruz)
    return res.text

santaCruz = get_text1()

santaCruz = bs4.BeautifulSoup(santaCruz)

santaCruz = santaCruz.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

santaCruz0 = santaCruz[0].text
santaCruz1 = santaCruz[1].text
santaCruz = santaCruz0 + '. ' + santaCruz1 + '.'
santaCruz = html2text.html2text(santaCruz)

santaCruzCA = "Santa Cruz, CA tide times - "
beaches[santaCruz] = santaCruzCA

#Fort Bragg
fortBragg = 'https://www.tideschart.com/United-States/California/Fort-Bragg/'
def get_text1():
    res = requests.get(fortBragg)
    return res.text

fortBragg = get_text1()

fortBragg = bs4.BeautifulSoup(fortBragg)

fortBragg = fortBragg.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

fortBragg0 = fortBragg[0].text
fortBragg1 = fortBragg[1].text
fortBragg = fortBragg0 + '. ' + fortBragg1 + '.'
fortBragg = html2text.html2text(fortBragg)

fortBraggCA = "Fort Bragg, CA tide times - "
beaches[fortBragg] = fortBraggCA

#Coronado
coronado = 'https://www.tideschart.com/United-States/California/Coronado/'
def get_text1():
    res = requests.get(coronado)
    return res.text

coronado = get_text1()

coronado = bs4.BeautifulSoup(coronado)

coronado = coronado.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

coronado0 = coronado[0].text
coronado1 = coronado[1].text
coronado = coronado0 + '. ' + coronado1 + '.'
coronado = html2text.html2text(coronado)

coronadoCA = "Santa Monica, CA tide times - "
beaches[coronado] = coronadoCA


#Santa Monica
santaMonica = 'https://www.tideschart.com/United-States/California/Santa-Monica/'
def get_text1():
    res = requests.get(santaMonica)
    return res.text

santaMonica = get_text1()

santaMonica = bs4.BeautifulSoup(santaMonica)

santaMonica = santaMonica.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

santaMonica0 = santaMonica[0].text
santaMonica1 = santaMonica[1].text
santaMonica = santaMonica0 + '. ' + santaMonica1 + '.'
santaMonica = html2text.html2text(santaMonica)

santaMonicaCA = "Santa Monica, CA tide times - "
beaches[santaMonica] = santaMonicaCA


#Laguna Beach
lagunaBeach = 'https://www.tideschart.com/United-States/California/Laguna-Beach/'
def get_text1():
    res = requests.get(lagunaBeach)
    return res.text

lagunaBeach = get_text1()

lagunaBeach = bs4.BeautifulSoup(lagunaBeach)

lagunaBeach = lagunaBeach.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

lagunaBeach0 = lagunaBeach[0].text
lagunaBeach1 = lagunaBeach[1].text
lagunaBeach = lagunaBeach0 + '. ' + lagunaBeach1 + '.'
lagunaBeach = html2text.html2text(lagunaBeach)

lagunaBeachCA = "Laguna Beach, CA tide times - "
beaches[lagunaBeach] = lagunaBeachCA

#Cambria
cambria = 'https://www.tideschart.com/United-States/California/Cambria/'
def get_text1():
    res = requests.get(cambria)
    return res.text

cambria = get_text1()

cambria = bs4.BeautifulSoup(cambria)

cambria = cambria.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

cambria0 = cambria[0].text
cambria1 = cambria[1].text
cambria = cambria0 + '. ' + cambria1 + '.'
cambria = html2text.html2text(cambria)

cambriaCA = "Cambria, CA tide times - "
beaches[cambria] = cambriaCA


#Pismo
pismo = 'https://www.tideschart.com/United-States/California/Pismo-Beach/'
def get_text1():
    res = requests.get(pismo)
    return res.text

pismo = get_text1()

pismo = bs4.BeautifulSoup(pismo)

pismo = pismo.findAll('div', {'class':'feature-box fbox-left fbox-plain'})

pismo0 = pismo[0].text
pismo1 = pismo[1].text
pismo = pismo0 + '. ' + pismo1 + '.'
pismo = html2text.html2text(pismo)

pismoCA = "pismo, CA tide times - "
beaches[pismo] = pismoCA


#print(beaches)
# py -m pip install request 
# cmd to get request lib (module)
# py -m pip install regex
# cmd to get regex lib (module)
# py -m pip install pygal
# cmd to get charts lib (module)
# py -m pip install cairosvg
# cmd to get lib which makes png images (for charts)
import requests
import re
import pygal
import os


class RokPrzebieg:
	Rok = 0
	Przebieg = 0

url = 'https://www.olx.pl/motoryzacja/samochody/q-transporter-t3/'
response = requests.get(url)
#print(response.text)

#matchLinkRegex = '<a class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLinkPromoted "[\S\s]*href="([\S\s]*)" title="" >'
matchLinkRegex = 'href="(https:\/\/www.olx.pl\/oferta.*?\.html#\w*?)"'
rokProdukcjiRegex = 'Rok produkcji[\s\S]*?<strong>[\s\S]*?(\d\d\d\d)'
przebiegRegex = 'Przebieg[\s\S]*?<strong>[\s\S]*?\s*([\d\s]+)'
matches = re.findall(matchLinkRegex, response.text)
print('Matches:')
print(matches)
i = 0


dane = list()
for match in matches:
	print(i)
	print(match)
	responseOffer = requests.get(match)
	#print(responseOffer.text)
	przebiegMatch = re.search(przebiegRegex, responseOffer.text)
	rokProdukcjiMatch = re.search(rokProdukcjiRegex, responseOffer.text)
	
	przebieg = przebiegMatch.group(1)
	rokProdukcji = rokProdukcjiMatch.group(1)
	print('Rok: ',rokProdukcji)
	print('Przebieg: ',przebieg)
	
	rp = RokPrzebieg()
	rp.Rok = int(rokProdukcji.strip())
	rp.Przebieg = int(przebieg.strip().replace(' ',''))
	if(rp.Przebieg > 1000000):
		print("Przebieg nierealny. Oferta nie zostanie uwzgledniona w wykresie")
		continue
		
	dane.append(rp)
	i = i + 1
	
graph = pygal.XY(stroke=False);
graph.Title = 'Rok a przebieg'

graph.add('', [(d.Rok, d.Przebieg) for d in dane])

fileName = 'wykres.svg'
graph.render_to_file(fileName)
os.system(fileName);



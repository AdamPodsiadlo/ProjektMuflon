# py -m pip install request 
# cmd to get request lib (module)
# py -m pip install regex
# cmd to get request lib (module)
import requests
import re


class RokPrzebieg:
	Rok = ""
	Przebieg = ""

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
	rp.Rok = rokProdukcji
	rp.Przebieg = przebieg
	
	dane.append(rp)
	i = i + 1
	
	




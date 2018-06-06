# python -m pip install request 
# cmd to get request lib (module)
# python -m pip install regex
# cmd to get request lib (module)
import requests
import re
url = 'https://www.olx.pl/motoryzacja/samochody/q-transporter-t3/'
response = requests.get(url)
#print(response.text)

#matchLinkRegex = '<a class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLinkPromoted "[\S\s]*href="([\S\s]*)" title="" >'
matchLinkRegex = 'summary[\S\s]*?href="([\S\s]*?)"'
matches = re.findall(matchLinkRegex, response.text)
print('Matches:')
print(matches)
i = 0
for match in matches:
	print(i)
	print(match)
	i = i + 1




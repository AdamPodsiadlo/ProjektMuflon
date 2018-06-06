# python -m pip install request 
# cmd to get request lib (module)
import requests
url = 'https://www.olx.pl/motoryzacja/samochody/q-transporter-t3/'
response = requests.get(url)
print(response.text)
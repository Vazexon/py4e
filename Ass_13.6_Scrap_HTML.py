from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import xml.etree.Element

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
for x in range(0, 7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[17].get('href', None)
    print(url, tags[17].contents[0])
    print('...')

print('Name:', tags[17].contents[0])

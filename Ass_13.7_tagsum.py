import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#if api_key is False:
#    api_key = 42
#    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
#else :
#    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_387344.xml'#http://py4e-data.dr-chuck.net/comments_387344.xml
xml = urlopen(url, context=ctx).read()
stuff = ET.fromstring(xml)
lst = stuff.findall('comments/comment')
print('Counts:', len(lst))
total = 0
for count in lst:
    value = int(count.find('count').text)
    total += value
print('Total counts:', total)

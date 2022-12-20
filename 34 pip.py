
import urllib.request

req= urllib.request.urlopen('https://tsn.ua/ato/okupanti-za-dobu-mayzhe-30-raziv-atakuvali-hersonschinu-ye-poraneniy-ova-2215384.html')
html=req.read()

print(html)

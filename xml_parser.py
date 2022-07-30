#import modules
import urllib.request as url
import xml.etree.ElementTree as et

#python 3 has adoptiuon to this library if you use python two this will be diffrent sytax
with url.urlopen("http://www.w3schools.com/xml/cd_catalog.xml") as data:
    web_data = data.read()
    xml_data = et.fromstring(web_data)
    cd_list = xml_data.findall("CD")

for x in cd_list:
    print(x.find("TITLE").text,x.find("PRICE").text)
#accessing other aspect of the same xml data with diffrent tags
#alos wrap the in float to make the data useable in arthmetic

def addupnumber(A):
    results = 0
    for x in A:
        results = results+x
    return results


cd_prices = []
for x in cd_list:
    cd_prices.append(float(x.find("PRICE").text))
print(addupnumber(cd_prices))

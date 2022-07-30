#import modules
import urllib.request as url

#python 3 has adoptiuon to this library if you use python two this will be diffrent sytax
with url.urlopen("https://docs.python.org/2/library/urllib.html") as data:
    web_data = data.read()
    print(web_data)

#url retrive c an alos be used to download the whole resoures filr itself
web_dataFile = url.urlretrieve("https://docs.python.org/2/library/urllib.html","python.html")
print(web_dataFile)

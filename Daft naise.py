#call the libraries that we need
from bs4 import BeautifulSoup
import urllib
import csv
import time
import json

writer = csv.writer(open("daft.csv", "a"))
writer.writerow(["Name", "Area", "Price", "Latitude", "Longitude"])
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
nextpage=0

while True:
    url = urllib.urlopen('http://www.daft.ie/dublin/commercial-property-for-rent/retail-units-for-rent/?searchSource=commercial&offset='+str(nextpage)).read()
    soup1 = BeautifulSoup(url, "html.parser")

    for container in soup1.find_all('div', attrs={'class': 'search_result_title_box'}):
        abc = container.a['href']
        link=urllib.urlopen('http://www.daft.ie'+str(abc)).read()
        #print link
        soup = BeautifulSoup(link,"html.parser")

        try:
            Name = soup.find('h1').text.strip()
            Name = Name.encode("ascii",'ignore')
            print ("Name  : " + Name)
        except Exception:
            print ("Name : NA")
        try:
            price = soup.find('div', {'id': 'smi-price-string'}).text
            price = price.encode("ascii", 'ignore')
            print ("Price : " + price)
        except Exception:
            print ("Price : Contact Us")
        try:
            Type = soup.find('span', {'class': 'header_text'}).text
            Type = Type.encode("ascii", 'ignore')
            print ("Type  : " + Type)
        except Exception:
            print ("Type : Contact Us")
        try:
            Area = soup.find('span', {'class': 'header_text'})  # ('span', {'class': 'bar'})
            if Area:
                area = Area.findNext('span', {'class': 'header_text'}).text
                area = area.encode("ascii", 'ignore')
                print ("Area  : " + area)
        except Exception:
            print ("Area : Contact Us")

       # writer.writerow([ Name, price, area, Type])

        #while True:
            #address = raw_input('Enter location: ')
            #if len(address) < 1: break

        url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': Name})
            # print 'Retrieving', url
        uh = urllib.urlopen(url)
        data = uh.read()
            # print 'Retrieved',len(data),'characters'

        try:
            js = json.loads(str(data))

        except:
            js = None
        if 'status' not in js or js['status'] != 'OK':
            print '==== Failure To Retrieve ===='
                # print data
            continue

        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print 'lat', lat, 'lng', lng
        writer.writerow([Name, area, price, lat, lng])
    if soup1.find('h1').text == 'No results':
        print ("Finished")
        exit()
    else:
        nextpage += 20
        continue
    time.sleep(5)
#call the libraries that we need
from bs4 import BeautifulSoup
import urllib
import csv
import time

writer = csv.writer(open("Zoopla.csv", "w"))
writer.writerow(["Name", "Area", "Price", "Latitude", "Longitude"])
url = urllib.urlopen("http://www.zoopla.co.uk/to-rent/commercial/retail-premises/london/?identifier=london&property_type=retail&page_size=100&q=london&search_source=refine&floor_area_units=sq_feet&radius=0&pn=1")
soup = BeautifulSoup(url, "html.parser")

lastelement= soup.find('span', attrs={'class': 'listing-results-utils-count'})
lastpage=int(lastelement.text.split('of')[1])/100+1

for ptemp in range(1,lastpage):
    urlitem = urllib.urlopen("http://www.zoopla.co.uk/to-rent/commercial/retail-premises/london/?identifier=london&property_type=retail&page_size=100&q=london&search_source=refine&floor_area_units=sq_feet&radius=0&pn="+str(ptemp))
    soup1 = BeautifulSoup(urlitem, "html.parser")
    for container in soup1.find_all('div', attrs={'class': 'status-wrapper'}):
            abc = container.a['href']
            link = urllib.urlopen('http://www.zoopla.co.uk' + str(abc))
            soup2 = BeautifulSoup(link, "html.parser")
            Name = soup2.find('div', attrs={'class': 'listing-details-address'})
            if Name:
                try:
                    name=Name.find('h2').text.strip()
                    name = name.encode("ascii", 'ignore')
                except Exception:
                    name=''
                print("Name :" + name)
                try:
                    Area=Name.find('span').text.strip()
                    Area = Area.encode("ascii", 'ignore')
                except Exception:
                    Area=''
                print ("Area : "+ Area)
            try:
                Price=soup2.find('div',attrs={'class':'listing-details-price text-price'}).text.strip()
                Price = Price.encode("ascii", 'ignore')
                if "Non-quoting" in Price or "POA" in Price:Price =" NA"
                #else:print("price : " + Price)
            except Exception:
                Price=''
            print("Price :" + Price)
            try:
                if soup2.find('span', attrs={'class' :'listing-results-just-added'}):
                    new= soup2.find('span', attrs={'class' :'listing-results-just-added'}).text.strip()
                else : new =''
                print "New Space : ", new
            except Exception:
                print "NA"

            latitudelist = soup2.findAll('meta', attrs={'itemprop': 'latitude'}) #<meta itemprop="latitude" content="51.52604">
            for latitude in latitudelist:  lat = latitude['content'].encode("ascii", 'ignore')
            longitudelist = soup2.findAll('meta', attrs={'itemprop': 'longitude'})
            for longitude in longitudelist: lng = longitude['content'].encode("ascii", 'ignore')
            print "Latitude, Longitude :", lat + "," + lng

            writer.writerow([name, Area, Price, lat, lng])


    time.sleep(5)



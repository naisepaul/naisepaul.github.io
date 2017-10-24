from bs4 import BeautifulSoup
import urllib
import csv
import time
import json
import pyodbc

nextpage=1
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#writer = csv.writer(open("property.csv", "w")) # a for appending
#writer.writerow(["Name", "Price", "Area", "Type", "Latitude", "Longitude"])

while True:
    url = urllib.urlopen('http://www.property.ie/commercial-property/dublin/type_retail-unit/commercial-ad-to-let/p_'+str(nextpage)).read()
    soup1 = BeautifulSoup(url, "html.parser")

    for container in soup1.find_all('div', attrs={'class': 'search_result'}):
        try:
            Name = container.find('a').text.strip()
            Name = Name.encode("ascii", 'ignore')
            print("Name   : " + Name)
        except Exception:
            Name = 'Contact Us'
            print ("Name : " + Name)
        try:
            Price = container.find('h3').text.strip()
            Price = Price.encode("ascii", 'ignore')
            print("Price  : " + Price)
        except Exception:
            Price='Contact Us'
            print ("Price : "+Price)
        try:
            type = container.find('h4').text.strip()
            type = type.encode("ascii")
            #area,type=type.split(')')
            type = type.split(')')
            area=type[0]
            type = type[1]
            print ("Area   : " + area + ")")
            print ("Type   :" + type)
        except Exception:
            area= 'Contact Us'
            type= 'Contact Us'
            print ("Area   : "+area)
            print ("Type   : "+type)

#GETTING LONGITUDE AND LADITUDE
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
            #print '==== Failure To Retrieve ===='
            lat = 'Contact Us'
            lng = 'Contact Us'
                # print data
            continue

        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print 'lat', lat, 'lng', lng


        #with open('inaise.csv', 'a') as csv_file:
        #writer = csv.writer(csv_file)

 #       writer.writerow([Name, Price, area+")", type, lat, lng])


        '''
        #import pyodbc
        import pymssql
        server = 'tutorialtestserver.database.windows.net'
        database = 'Property Details'
        username = 'sqla&&&&'
        password = '&&&1234'
        driver= '{ODBC Driver 13 for SQL Server}'
        cnxn = pymssql.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("INSERT INTO PropertyListings (Name, Area, Latitude, Longitude) VALUES ('Jervis', '300', , 53.45776, -6.5678)")
        cnxn.commit()

        #cnxn.rollback()
 '''
    if soup1.find('div', attrs = {'id': 'noresults_refine'}):
        print ("Finished")
        exit()
    else:
        nextpage += 1
        continue
    time.sleep(5)

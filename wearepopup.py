#call the libraries that we need
from bs4 import BeautifulSoup
import urllib
import csv
import time
import pyodbc


#writer = csv.writer(open("wearepopup.csv", "w"))
#writer.writerow(["Name", "Area", "Price", "Latitude", "Longitude"])
url = urllib.urlopen("http://wearepopup.com/search/spaces/?tenancy=&location=c%7CLondon&price_min=&price_max=&size_min=&size_max=&measuring=ft&q=&order=date&page=1")
soup = BeautifulSoup(url, "html.parser")
lastelement= soup.find('span', attrs={'class': 'result_count'}).text
lastpage=int(lastelement)/20+1
#print lastpage
for ptemp in range(1,lastpage):
    urlitem = urllib.urlopen("http://wearepopup.com/search/spaces/?tenancy=&location=c%7CLondon&price_min=&price_max=&size_min=&size_max=&measuring=ft&q=&order=date&page="+str(ptemp))
    soup1 = BeautifulSoup(urlitem, "html.parser")
    for container in soup1.find_all('div', attrs={'class': 'prop-box'}):
        abc = container.a['href']
        link = urllib.urlopen('http://wearepopup.com' + str(abc))
        soup2 = BeautifulSoup(link, "html.parser")
        try:
            Name = soup2.find('h1').text.strip()
            Name = Name.encode("ascii", 'ignore')
        except Exception:
            Name = ''
        print("Name : " + Name)
        try:
            Price= soup2.find('div',attrs={'class':'amount'}).text.strip()  #.split('from')[1].split('/')[0]  #split if we need only price value
            Price = Price.encode("ascii", 'ignore')
        except Exception:
            Price = ''
        print("Price : " + Price)
        try:
            Area = soup2.find('li').text.strip()#.split('(')[0]  # spliting sq. feet
            Area = Area.encode("ascii", 'ignore')
        except Exception:
            Area = ''
        print("Area  : " + Area)
        try:
            locationlist = soup2.findAll('div', attrs={'id': 'map'})
            for location in locationlist:
                lat = location['data-lat']
                lng = location['data-lng']

        except Exception:
            lat = ''
            lng = ''
        print("Latitude : " + lat)
        print("Longitude : " + lng)

 #       writer.writerow([Name, Area, Price, lat, lng])

        server = 'tutorialtestserver.database.windows.net'
        database = 'Property Details'
        username = 'sqladmin'
        password = 'Test1234'
        driver = '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect('DRIVER=' + driver + ';PORT=1433;SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        # cursor.execute("BEGIN TRANSACTION")
        #id = cursor.lastrowid

        cursor.execute("INSERT INTO dbo.Properties (Name,Area,Price,Latitude,Longitude,Website) VALUES (?,?,?,?,?,?)", (Name,Area,Price,lat,lng,'Wearepopup'))
        # cnxn.rollback()
        #print "done"
        cnxn.commit()
'''
        cur.execute("'INSERT OR IGNORE INTO Follows
                    (from_id, to_id)
        VALUES(?, ?)"', (id, friend_id) )
        Again
        we
        simply
        tell
        the
        database
        to
        ignore
        our
        attempted
        INSERT if it
        would
        violate
        the
        uniqueness
        constraint
        that
        we
        specified
        for the Follows rows.  '''


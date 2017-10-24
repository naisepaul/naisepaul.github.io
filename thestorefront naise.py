from selenium import webdriver
import time
import csv
# create a new Firefox session
driver = webdriver.PhantomJS()
driver.implicitly_wait(30)
#driver.maximize_window()
results = []

writer = csv.writer(open("thestorefront.csv", "a"))
writer.writerow(["Name", "Area", "Price", "Latitude", "Longitude"])
driver.get("https://app.thestorefront.com/listings?address=London,%20UK&zoom=10&parent_project_type_id=5&latitude=51.5073509&longitude=-0.12775829999998223&lat_g=51.38494009999999&lat_l=51.6723432&lng_g=-0.351468299999965&lng_l=0.1482710999999881&s=score%20DESC&page=1")
LastElement=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[4]/div[1]/ul/li[5]")
LastElementNumber=(int(LastElement.text))
RollingPages=LastElementNumber+1
#print RollingPages
for ptemp in range(1,RollingPages):
    driver.get("https://app.thestorefront.com/listings?address=London,%20UK&zoom=10&parent_project_type_id=5&latitude=51.5073509&longitude=-0.12775829999998223&lat_g=51.38494009999999&lat_l=51.6723432&lng_g=-0.351468299999965&lng_l=0.1482710999999881&s=score%20DESC&page="+str(ptemp))
    for e in driver.find_elements_by_css_selector("[data-listing-id]"):
        A = e.get_attribute("data-listing-id")
        results.append(A)

for each in results:
    driver.get("https://app.thestorefront.com/listings/" + str(each))
    # time.sleep(1)
    Name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div[1]").text
    Name = Name.encode("ascii", 'ignore')
    print("Name :", Name)
    try:
        Price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]").text
        Price = Price.encode("ascii", 'ignore')
        print("Price :", Price)
    except Exception:
        Price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/span").text
        Price = Price.encode("ascii", 'ignore')
        print("Price :", Price)
    try:
        Area = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]").text
        Area = Area.encode("ascii", 'ignore')
        print("Area :", Area)
    except Exception:
        Area = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div[2]/div[1]/div[3]/div[2]").text
        Area = Area.encode("ascii", 'ignore')
        print("Area :", Area)
    Maps = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div[2]/a")
    link = Maps.get_attribute("href")
    a, b = link.split(",")
    c, lat = a.split("=")
    lng, d = b.split("&z")
    lat = lat.encode("ascii", 'ignore')
    lng = lng.encode("ascii", 'ignore')
    A = [lat, lng]
    print("[Latitude, Longitude] :", A)

    writer.writerow([Name, Area, Price, lat, lng])


    '''
    driver.get("https://app.thestorefront.com/listings?address=London,%20UK&zoom=10&parent_project_type_id=5&latitude=51.5073509&longitude=-0.12775829999998223&lat_g=51.38494009999999&lat_l=51.6723432&lng_g=-0.351468299999965&lng_l=0.1482710999999881&s=score%20DESC&page="+str(ptemp))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    datalisting= soup.findAll('div',attrs={'class':'favorite-tag ng-isolate-scope'})
    for e in datalisting:
        A = e['data-listing-id']
        driver.get('https://app.thestorefront.com/listings/' + str(A))
        soup1 = BeautifulSoup(driver.page_source, "html.parser")
        Name = soup1.find('div', attrs={'class': 'title ng-binding'}).text
        print Name'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
page = requests.get(START_URL)
print(page)

browser.get(START_URL)
time.sleep(10)
stars_data = []

soup = BeautifulSoup(browser.page_source, "html.parser")
table = soup.find('table')

temp_list = []
tablerows = table.find_all("tr")

for tr in tablerows:

            td_tags = tr.find_all("td")
            row = [i.text.rstrip() for i in td_tags]
            temp_list.append(row)

star_name = []
radius = []
mass = []
distance = []

for i in range(1,len(temp_list)):
    star_name.append(i[1])
    radius.append(i[6])
    mass.append(i[5])
    distance.append(i[3])

df = pd.DataFrame(list(zip(star_name,radius,mass,distance)),columns = ['Proper_name','Distance','Mass','Radius'])
print(df)
df.to_csv('star_info.csv')

                # if index == 0:                   
                #     temp_list.append(td_tag.find_all("a")[0].contents[0])
                # else:
                #     try:
                #         temp_list.append(td_tag.contents[0])
                #     except:
                #         temp_list.append("")

            






# headers = ["proper_name", "distance", "visual_magnitude", "spectral_type"]
# planets = pd.DataFrame(stars_data,columns=headers)
# planets.to_csv('starsinfo.csv',index=True,index_label='label')
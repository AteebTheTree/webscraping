import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

results = []
driver = webdriver.Chrome(executable_path="C:/Users/15146/PycharmProjects/pythonProject/chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
content = driver.page_source
soup = BeautifulSoup(content)

for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    name = tds[1].text
    new_name = name.strip('\n')
    distance = tds[3].text
    new_distance = distance.strip('\n')
    mass = tds[5].text
    new_mass = mass.strip('\n')
    radius = tds[6].text
    new_radius = radius.strip('\n')
    results.append([new_name, new_distance, new_mass, new_radius])
df = pd.DataFrame(results)
df.to_csv("planets.csv")



from email import header
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL= 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser=webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    header=[
        "vmag",
        "name",
        "bayer_designation",
        "distance",
        "spectral_class",
        "mass",
        "radius",
        "lumonisity"
    ]
    star_data=[]

    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("tr", attrs={"class", "expoplanet"}):
            th_tags = tr_tag.find_all("th")
            temp_list = []
            # enumerate is a counter. It will count how many object there are. Inside a li function if there are 4 data, it will show 4.
            for index, th_tag in enumerate(th_tags):
                if index == 0:
                    temp_list.append(th_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(th_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
            # xpath is used to navigate through elements or pages.
            browser.find_element_by_xpath(
                '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a'
            ).click()

with open("data.csv", "w") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(star_data)
    
scrape()

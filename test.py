# import time
# import bios
import csv
# import parseCsv
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
list = []
rrp = []


def scrapeBahutSara(url):
    option = webdriver.FirefoxOptions()
    option.headless = True
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
    driver.get(url)
    driver.implicitly_wait(2)
    pds = []
    profileHandle = " "
    profileImgLink = " "
    postCount = " "
    profileFollowers = " "
    profileFollowing = " "
    profileNameMentioned = " "
    profileBios = " "

    try:
        profileHandle = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/h2").text

    except:
        print("")
    # pds.append(profileHandle)
    try:
        profileImgLink = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/div/div/div/button/img").get_attribute("src")
        # print(profileImgLink)

    except:
        print("")
    try:
        postCount  = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span").text
        print(postCount)

    except:
        print("")
    try:
        profileFollowers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text
        print(profileFollowers)

    except:
        print()
    try:
        profileFollowing = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
        print(profileFollowing)

    except:
        print()
    try:
        profileNameMentioned = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/h1").text
        print(profileNameMentioned)

    except:
        print()
    try:
        profileBios = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/span").text
        print(profileBios)
    except:
        print()
    pds.append(profileHandle)
    pds.append(profileImgLink)
    pds.append(postCount)
    pds.append(profileFollowers)
    pds.append(profileFollowing)
    pds.append(profileNameMentioned)
    pds.append(profileBios)

    rrp.append(pds)
    driver.close()
    # pds.append(hrefs)
# cc = pd.read_csv('rir.csv', header=None)
i=0

with open("rir.csv", 'r') as csvfile:
    datareader = csv.reader(csvfile)
    url1 = None
    url2 = None
    for row in datareader:
        if i>1000:
            break
        list.append(row[0])
        i=i+1
        # print(row[0])
i=117
while i<=200:
    try:
        scrapeBahutSara(list[i])
        scrapeBahutSara(list[i+1])
        print(i)
    except:
        print()
    i=i+2
# print(cc['profile_url'])
# scrapeBahutSara("https://www.instagram.com/poulami2306/")
print(rrp)
df = pd.DataFrame(rrp, columns=['profileHandle','profileImgLink','postCount','profileFollowers','profileFollowing','profileNameMentioned','profileBios'])
df.to_csv('./rss'  + '.csv', index=False)



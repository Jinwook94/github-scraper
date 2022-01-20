from random import randint

import chromedriver_autoinstaller
import lxml
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from lxml import etree, html
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


from data import keywordsDict, repoDict

# Excel File Export Config
wb = Workbook()
ws1 = wb.active
ws1.title = "github_scraper" # Name of excel sheet
ws1.append(["Categories", "Keywords", "Repositories", "Counts", "URLs"])    # First row in excel sheet

# Scrapping all github



for (keyword, category) in keywordsDict.items():
    url = 'https://github.com/search?q=' + keyword + '&type=Code'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    driver.get(url)
    div_elems = driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[2]/div[1]/ul/li[5]/a/span')
    print(div_elems)




#     try:
#         ws1.append([category, keyword, 'All GitHub', counts.text, url])
#         print("<Completed> Keyword: " + keyword + ", Repo: " + 'All GitHub')
#     except Exception as e:
#         print("Error: ", end="")
#         print(data)
#         print("       keyword= " + keyword + ", repo=" + 'All GitHub')
#         print("       url= " + url)
#         ws1.append([category, keyword, 'All GitHub', "Error", url])
#         continue
# #
# # Scrapping
# for (keyword, category) in keywordsDict.items():
#     for (repo, org) in repoDict.items():
#         url = 'http://www.github.com/' + org + '/' + repo + '/' + 'search?l=Java&q=' + keyword
#
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#         }
#
#         time.sleep(randint(10, 20))  # To avoid HTTP 429: Too Many Requests response
#
#         data = requests.get(url, headers=headers)
#
#         soup = BeautifulSoup(data.text, 'html.parser')
#         counts = soup.select_one(
#             '#repo-content-pjax-container > div > div.col-12.col-md-3.float-left.px-md-2 > nav.menu.border.d-none.d-md-block > a.menu-item.selected > span')
#
#         try:
#             ws1.append([category, keyword, repo, counts.text, url])
#             print("<Completed> Keyword: " + keyword + ", Repo: " + repo)
#         except Exception as e:
#             print("Error: ", end="")
#             print(data)
#             print("       keyword= " + keyword + ", repo=" + repo)
#             print("       url= "+url)
#             ws1.append([category, keyword, repo, "Error", url])
#             continue

#
# # Excel File Naming
# now = datetime.now()
# month = str(now.month).zfill(2)
# day = str(now.day).zfill(2)
# hour = str(now.hour).zfill(2)
# minute = str(now.minute).zfill(2)
# filename = "github_scraper_" + month + day + "_" + hour + minute + ".xlsx"
#
# # Excel File Export
# wb.save(r'files/' + filename)
# print(filename + ", Save Completed")

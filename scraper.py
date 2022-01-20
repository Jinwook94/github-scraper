from random import randint

import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from openpyxl import Workbook

from data import keywordsDict, repoDict

# Excel File Export Config
wb = Workbook()
ws1 = wb.active
ws1.title = "github_scraper" # Name of excel sheet
ws1.append(["Category", "Keyword", "Organization", "Repository", "Count", "URL"])    # First row in excel sheet

# Scrapping
for (keyword, category) in keywordsDict.items():
    for (repo, org) in repoDict.items():
        url = 'http://www.github.com/' + org + '/' + repo + '/' + 'search?l=Java&q=' + keyword

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }

        time.sleep(randint(5, 8))  # To avoid HTTP 429: Too Many Requests

        data = requests.get(url, headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')
        count = soup.select_one(
            '#repo-content-pjax-container > div > div.col-12.col-md-3.float-left.px-md-2 > nav.menu.border.d-none.d-md-block > a.menu-item.selected > span')

        try:
            ws1.append([category, keyword, org, repo, count.text, url])
            print("<Completed> Keyword: " + keyword + ", Repo: " + repo)
        except Exception as e:
            print("Error: ", end="")
            print(data)
            print("       keyword= " + keyword + ", repo=" + repo)
            print("       url= "+url)
            ws1.append([category, keyword, org, repo, "Error", url])
            continue

# Excel File Naming
now = datetime.now()
month = str(now.month).zfill(2)
day = str(now.day).zfill(2)
hour = str(now.hour).zfill(2)
minute = str(now.minute).zfill(2)
filename = "github_scraper_" + month + day + "_" + hour + minute + ".xlsx"

# Excel File Export
wb.save(r'files/' + filename)
print(filename + ", Save Completed")

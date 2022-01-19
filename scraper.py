from random import randint

import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Github Org Name : Github Repo Name
repoDict = {
    # Popular Open Source Projects Using Spring Framework
    'generator-jhipster': 'jhipster',
    'zipkin': 'openzipkin',
    'piggymetrics': 'sqshq',
    'thingsboard': 'thingsboard',
    'spring-boot-admin': 'codecentric',
    'cas': 'apereo',
    'spring-petclinic': 'spring-projects',
    'flowable-engine': 'flowable',
    'conductor': 'Netflix',
    'kafdrop': 'obsidiandynamics',
    'sagan': 'spring-io',
    'initializr': 'spring-io',
    'TelegramBots': 'rubenlagu',
    'shopizer': 'shopizer-ecommerce',
    'cwa-server': 'corona-warn-app',
    'BroadleafCommerce': 'BroadleafCommerce',
    'uaa': 'cloudfoundry',

    # Woowacourse Projects
    '2021-tyf': 'woowacourse-teams',
    '2021-jujeol-jujeol': 'woowacourse-teams',
    '2021-drop-the-code': 'woowacourse-teams',
    '2021-botobo': 'woowacourse-teams',
    '2021-zzimkkong': 'woowacourse-teams',
    '2021-babble': 'woowacourse-teams',
    '2021-gpu-is-mine': 'woowacourse-teams',
    '2021-pick-git': 'woowacourse-teams',
    '2021-cvi': 'woowacourse-teams',
    '2021-nolto': 'woowacourse-teams',
    '2021-darass': 'woowacourse-teams',
    '2021-see-you-there': 'woowacourse-teams',
    '2020-taggle': 'woowacourse-teams',
    '2020-doran-doran': 'woowacourse-teams',
    '2020-legeno-around-here': 'woowacourse-teams',
    '2020-saebyeok': 'woowacourse-teams',
    '2020-devbie': 'woowacourse-teams',
    '2020-zeze': 'woowacourse-teams',
    '2020-14f-guys': 'woowacourse-teams',
    '2020-6rinkers': 'woowacourse-teams',
    '2020-songpa-people': 'woowacourse-teams',
    '2020-seller-lee-company': 'woowacourse-teams',
}

# Search Keywords : Keywords Category
keywordsDict = {
    # Annotations
    'override': 'Annotation Default',
    'suppresswarnings': 'Annotation Default',
    'safevarargs': 'Annotation Default',
    'functionalinterface': 'Annotation Default',

    # Exceptions

    # Collections
    'java.util.ArrayList': 'Collections',
    'java.util.Vector': 'Collections',
    'java.util.LinkedList': 'Collections',
    'java.util.Stack': 'Collections',
    'java.util.HashSet': 'Collections',
    'java.util.TreeSet': 'Collections',
    'java.util.HashMap': 'Collections',
    'java.util.HashTable': 'Collections',
    'java.util.TreeMap': 'Collections',
    'java.util.Properties': 'Collections',

    # Collections Related
    'java.util.Iterator': 'Collections Related',
    'java.util.ListIterator': 'Collections Related',
    'java.util.Enumeration': 'Collections Related',
    'java.util.Comparator': 'Collections Related',

    #

}

# Excel File Export Config
wb = Workbook()
ws1 = wb.active
ws1.title = "github_scraper"
ws1.append(["Categories", "Keywords", "Repositories", "Counts", "URLs"])

# Scrapping
for (keyword, category) in keywordsDict.items():
    for (repo, org) in repoDict.items():
        url = 'http://www.github.com/' + org + '/' + repo + '/' + 'search?l=Java&q=' + keyword

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }

        time.sleep(randint(10, 20))  # To avoid HTTP 429: Too Many Requests response

        data = requests.get(url, headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')
        counts = soup.select_one(
            '#repo-content-pjax-container > div > div.col-12.col-md-3.float-left.px-md-2 > nav.menu.border.d-none.d-md-block > a.menu-item.selected > span')

        try:
            ws1.append([category, keyword, repo, counts.text, url])
            print("<Completed> Keyword: " + keyword + ", Repo: " + repo)
        except Exception as e:
            print("Error: ", end="")
            print(data)
            print("Error keyword=" + keyword+ ", Error repo=" + repo)
            ws1.append([category, keyword, repo, "Error", url])
            continue


#File Naming
now = datetime.now()
month = str(now.month).zfill(2)
day = str(now.day).zfill(2)
hour = str(now.hour).zfill(2)
minute = str(now.minute).zfill(2)
filename = "github_scraper_" + month + day + "_" + hour + minute + ".xlsx"

# Excel File Export
wb.save(r'files/'+filename)
print(filename+", Save Completed")


from random import randint

import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Github Org Name : Github Repo Name
repoDict = {
    'zipkin': 'openzipkin',
    'generator-jhipster': 'jhipster',
    'thingsboard': 'thingsboard',
    'sagan': 'spring-io',
    '2021-jujeol-jujeol': 'woowacourse-teams',
    '2021-botobo': 'woowacourse-teams',
    '2021-pick-git': 'woowacourse-teams',
    '2021-darass': 'darass-team',
    '2020-6rinkers': 'woowacourse-teams'
}

# Search Keywords : Keywords Category
keywordsDict = {
    'override': 'Annotation Default',
    'suppresswarnings': 'Annotation Default',
    'safevarargs': 'Annotation Default',
    'functionalinterface': 'Annotation Default',

}

# Excel File Export Config
wb = Workbook()
ws1 = wb.active
ws1.title = "urlGenerator"
ws1.append(["Keywords", "Repositories", "URLs"])

# Generate URLs
for (keyword, category) in keywordsDict.items():
    for (repo, org) in repoDict.items():
        url = 'http://www.github.com/' + org + '/' + repo + '/' + 'search?l=Java&q=' + keyword
        ws1.append([keyword, repo, url])

# File Naming
now = datetime.now()
month = str(now.month).zfill(2)
day = str(now.day).zfill(2)
hour = str(now.hour).zfill(2)
minute = str(now.minute).zfill(2)
filename = "urlGenerator_" + month + day + "_" + hour + minute + ".xlsx"

# Excel File Export
wb.save(r'files/'+filename)
print(filename + ", Save Completed")


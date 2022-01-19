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
wb.save(r'files/' + filename)
print(filename + ", Save Completed")

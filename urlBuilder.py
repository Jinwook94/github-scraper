from datetime import datetime
from openpyxl import Workbook

# Github Org Name : Github Repo Name


# Excel File Export Config
from data import keywordsDict, repoDict

# Excel File Config
wb = Workbook()
ws1 = wb.active
ws1.title = "urlBuilder"
ws1.append(["Keywords", "Repositories", "URLs"])

# URL Building
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
filename = "urlBuilder_" + month + day + "_" + hour + minute + ".xlsx"

# Excel File Export
wb.save(r'files/' + filename)
print(filename + ", Save Completed")

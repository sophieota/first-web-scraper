import csv
import requests
from BeautifulSoup import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

year = ['2015-2016', '2014-2015', '2013-2014', '2012-2013', '2011-2012', '2010-2011']
urlp1 = "https://columbian.gwu.edu/"
url = urlp1 + str(year)
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("college.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["department", "faculty", "sponsor", "title"])
writer.writerows(list_of_rows)
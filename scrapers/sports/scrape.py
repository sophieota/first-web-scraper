import csv
import requests
from BeautifulSoup import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

months = ['01', '02', '03', '04']
list_of_rows = []

for month in months:
    print month
    response = requests.get("http://m.nationals.mlb.com/roster/transactions/2017/" + month)
    html = response.content

    soup = BeautifulSoup(html)
    table = soup.find('table')

    for row in table.findAll('tr')[1:]:
        list_of_cells = []
        list_of_cells.append(month)
        for cell in row.findAll('td'):
            list_of_cells.append(cell.text.encode('utf-8'))
        list_of_rows.append(list_of_cells)
        for cell in row.findAll('a href'):
        	list_of_cells.append(cell.text.encode('utf-8'))
        list_of_rows.append(list_of_cells) 
        
outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["", "date", "url", "text"])
writer.writerows(list_of_rows)
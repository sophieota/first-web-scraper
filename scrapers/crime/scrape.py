import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html'
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

outfile = open("executions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["scheduled_executions", "link", "last_name", "first_name", "tdcj_number", "dob", "race", "date_received", "county"])
writer.writerows(list_of_rows)

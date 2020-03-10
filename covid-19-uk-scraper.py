import urllib.request
import urllib.parse
import json
import datetime
import csv

from bs4 import BeautifulSoup

url = 'https://www.gov.uk/api/content/government/publications/coronavirus-covid-19-number-of-cases-in-england/coronavirus-covid-19-number-of-cases-in-england'
f = urllib.request.urlopen(url)
response = json.loads(f.read().decode('utf-8'))
data = response['details']['body']

soup = BeautifulSoup(json.dumps(data), features="html.parser")
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
  columns = table_row.findAll(['th', 'td'])
  output_row = []
  for column in columns:
      output_row.append(int(column.text) if column.text.isnumeric() else column.text)
  output_rows.append(output_row)

raw_date = response['public_updated_at']
date = datetime.datetime.strptime(raw_date, '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%y-%m-%d')
    
with open(f'data/{date}.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
  writer.writerows(output_rows)

from datetime import datetime
from dateutil import parser

date = 'Febuary 1, 2018'
new_date = date.replace(',', ' ').split()
new_list = []
date = None
for data in new_date:
  if len(data) == 1:
    data = '0' + data
  new_list.append(data)
  date = '/'.join(new_list)

new_date = datetime.strptime(date, '%m/%d/%Y').date()
print(new_date)
from db_operations import DBOperations

db = DBOperations()

data_dict = {}
date = []
date_list = []
new_list = []
data_list = db.plotData(2018, 2020)

for data in data_list:
  date = data[0].split('-')
  if date[1] not in date_list:
    date_list.append(date[1])

for month in date_list:
  for data in data_list:
    date = data[0].split('-')
    if month == date[1]:
      new_list.append(data[1])
  data_dict.update({month: new_list})
  new_list = []

print(str(data_dict))

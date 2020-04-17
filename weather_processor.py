from db_operations import DBOperations
from plot_lib import makePlot
from make_dict import make_dict
import matplotlib.pyplot as plt
import numpy as np


class WeatherProcessor():

  def __init__(self):
    self.start_year = None
    self.end_year = None
    self.yes_no = None
    self.db_data = []
    self.data_base_made = False
    self.date_list = []
    self.new_list = []
    self.data_dict = {}

  def startUp(self):
    self.yes_no =  input("Do you want to dowload weather information(Y/N): ")

    if self.yes_no == 'Y' and not self.data_base_made:
      db = DBOperations()
      db.createTable()
      self.db_data = make_dict()
      db.insertData(self.db_data)
      self.data_base_made = True
      self.db_data_list = []

    if self.yes_no == 'N' or self.data_base_made:
      pass

    self.makePlot()

  def makePlot(self):
    self.start_year = input('Enter start year for weather data: ')
    self.end_year = input('Enter end year for weather data: ')

    db = DBOperations()
    data_dict = {}
    date = []
    date_list = []
    new_list = []
    data_list = db.plotData(self.start_year, self.end_year)
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
    print(data_dict)
    data = []
    for k, v in data_dict.items():
      data.append(v)
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low), 0)
    data.shape = (-1, 1)

    fig, ax1 = plt.subplots(figsize=(10, 6))
    fig.canvas.set_window_title('A Boxplot Example')
    ax1.set_title('Monthly Temperature Distribution for: {} to {} '.format(self.start_year, self.end_year))
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Temperature (Celsius)')
    ax1.boxplot(data)

    plt.show()


my_pro = WeatherProcessor()
my_pro.startUp()

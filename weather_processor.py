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

    if self.yes_no == 'N' or self.data_base_made:
      pass

    self.makePlot()

  def makePlot(self):
    self.start_year = input('Enter start year for weather data: ')
    self.end_year = input('Enter end year for weather data: ')

    db = DBOperations()

    self.db_data = db.plotData(self.start_year, self.end_year)

    for data in self.db_data:
      date = data[0].split('-')
    if date[1] not in self.date_list:
      self.date_list.append(date[1])

    for month in self.date_list:
      for data in self.db_data:
        date = data[0].split('-')
        if month == date[1]:
          self.new_list.append(data[1])
      self.data_dict.update({month: self.new_list})
      self.new_list = []

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
    ax1.boxplot(self.new_list)

    plt.show()


my_pro = WeatherProcessor()
my_pro.startUp()

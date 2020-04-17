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

    if not self.data_base_made:
      self.yes_no =  input("Do you want to dowload weather information(Y/N): ").upper()

      if self.yes_no == 'Y':
        db = DBOperations()
        db.createTable()
        self.db_data = make_dict()
        db.insertData(self.db_data)
        self.data_base_made = True
        self.db_data_list = []

    self.makePlot()

  def makePlot(self):
    self.start_year = input('Enter start year for weather data: ')
    self.end_year = input('Enter end year for weather data: ')

    db = DBOperations()
    monthCollection = {}
    data = []

    data_list = db.plotData(self.start_year, self.end_year)

    for date in  data_list:
      dateInfolist = date[0].split('-')
      if(str(dateInfolist[1]) not in monthCollection):
        monthCollection[dateInfolist[1]]=[]
      if(type(date[1]) is float):
        monthCollection[dateInfolist[1]].append(date[1])

    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low), 0)
    data.shape = (-1, 1)


    for k, v in monthCollection.items():
      data.append(v)

    fig, ax1 = plt.subplots(figsize=(10, 6))
    fig.canvas.set_window_title('A Boxplot Example')
    ax1.set_title('Monthly Temperature Distribution for: {} to {} '.format(self.start_year, self.end_year))
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Temperature (Celsius)')
    ax1.boxplot(data)
    plt.show()


my_pro = WeatherProcessor()
my_pro.startUp()

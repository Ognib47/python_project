"""
  Created by: Chris Podolsky
  WeatherProcessor class used to control flow of the application.
"""
from db_operations import DBOperations
from make_dict import make_dict
from plot_operations import PlotOperations

class WeatherProcessor():
  """
    Created by: Chris Podolsky
    WeatherProcessor class controls application flow.
  """
  def __init__(self):
    """
      Created by: Chris Podolsky
      Initialize variables used in the WeatherProcessor class.
    """
    self.start_year = None
    self.end_year = None
    self.yes_no = None
    self.db_data = []
    self.date_list = []
    self.new_list = []
    self.data_dict = {}
    self.plot = PlotOperations()
    self.db = DBOperations()

  def startUp(self):
    """
      Created by: Chris Podolsky
      Initial function that runs asks user if they want to create a weather
      data base.
    """
    self.yes_no =  input("Do you want to dowload weather information(Y/N): ").upper()

    if self.yes_no == 'Y':
      db = DBOperations()
      db.createTable()
      self.db_data = make_dict()
      db.insertData(self.db_data)
      self.db_data_list = []

    self.getUserData()

  def getUserData(self):
    """
      Created by: Chris Podolsky
      Takes user input passes it to Db function to return
      data needed to make the plot graph. Runs plot graph code.
    """
    self.start_year = input('Enter start year for weather data: ')
    self.end_year = input('Enter end year for weather data: ')
    self.plot.makePlot(self.db.plotData(self.start_year, self.end_year), self.start_year, self.end_year)

if __name__=="__main__":
  my_pro = WeatherProcessor()
  my_pro.startUp()

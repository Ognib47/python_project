"""
  Created By: Chris Podolsky
  Class used to make the box plot graph.
"""
import matplotlib.pyplot as plt
import numpy as np

class PlotOperations():

  def __init__(self):
    """
      This initializes variables for the PlotOperations class.
    """
    self.data_list = []

  def makePlot(self, plot_data, start_year, end_year):
    """
      Created By: Chris Podolsky
      This function takes in data recieved from the databse weather table
      Also take in two dates from the user input. This data is used to make
      the box plot that is displayed. Majority of the code is boiler plate
      code found in the example from Mathplotlib.
    """
    month = {}

    self.data_list = plot_data

    for date in  self.data_list:
      date_list = date[0].split('-')
      if(str(date_list[1]) not in month):
        month[date_list[1]] = []
      if(type(date[1]) is float):
        month[date_list[1]].append(date[1])

    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low), 0)
    data.shape = (-1, 1)

    data = []
    for k, v in month.items():
      data.append(v)

    fig, ax1 = plt.subplots(figsize=(10, 6))
    fig.canvas.set_window_title('A Boxplot Example')
    ax1.set_title('Monthly Temperature Distribution for: {} to {} '.format(start_year, end_year))
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Temperature (Celsius)')
    ax1.boxplot(data)
    plt.show()
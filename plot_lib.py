import matplotlib.pyplot as plt
import numpy as np
from db_operations import DBOperations

db = DBOperations()

def makePlot(start_year, end_year):
  # Plot part
  spread = np.random.rand(50) * 100
  center = np.ones(25) * 50
  flier_high = np.random.rand(10) * 100 + 100
  flier_low = np.random.rand(10) * -100
  data = np.concatenate((spread, center, flier_high, flier_low), 0)
  data.shape = (-1, 1)

  data = []
  for k, v in db.makePlotData(db.plotData(start_year, end_year)).items():
    data.append(v)
  print(data)
  # multiple box plots on one figure
 # print(data)
  plt.figure()
  plt.boxplot(data)
  plt.show()
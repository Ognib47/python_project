# from make_dict import make_dict
import matplotlib.pyplot as plt
import numpy as np
from db_operations import DBOperations
from plot_lib import makePlot

# dict_maker = make_dict
db = DBOperations()
# db.createTable()
# db_dict = make_dict()
# db.insertData(db_dict)
# db.printData()


# makePlot(2018, 2020)
print(db.plotData(2018, 2020))

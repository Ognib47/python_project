"""
  Created by: Chris Podolsky
  Data base operations class has data base methods for application.
"""
import sqlite3
class DBOperations():
  """
    Created by: Chris Podolsky
    Data base class for application.
  """

  def __init__(self):
    """
      Created by: Chris Podolsky
      Initialzies connection, cursor and variables
      used in the data base class.
    """

    self.conn = None
    self.cursor = None
    self.list = []

  def createTable(self):
    """
      Created by: Chris Podolsky
      This function creates a data base table for data
      to be insertersd into from the weather scraper class.
      If the table exists the table will be destroyed and recreated when called.
    """

    self.conn = sqlite3.connect("weather.sqlite")
    self.cursor = self.conn.cursor()
    self.cursor.execute("DROP TABLE IF EXISTS weather")
    self.cursor.execute("""create table IF NOT EXISTS weather
                (id integer primary key autoincrement not null,
                date text not null,
                location text not null,
                min_temp real not null,
                max_temp real not null,
                avg_temp real not null);
                """)

  def insertData(self, weather_data):
    """
      Created by: Chris Podolsky
      This function accepts a dictionary of
      key, values pairs and inserts the data into the weather table.
    """

    for date, date_info in weather_data.items():
      self.cursor.execute("insert into weather(date, location, min_temp, max_temp, avg_temp)values (?,?,?,?,?)",
                          (date, "Winnipeg,MB", date_info['min_temp'], date_info['max_temp'], date_info['mean_temp']))
    self.conn.commit()
    self.conn.close()

  def plotData(self, start_year, end_year):
    """
      Created by: Chris Podolsky
      This function querries the data base for data based on user input
      Returns a cursor for all data between the given years. Sorted into ascending order.
      This data is used in the creation of a box plot graph.
    """

    self.conn = sqlite3.connect("weather.sqlite")
    self.cursor = self.conn.cursor()
    _SQL = "select date, avg_temp from weather where date BETWEEN '{}-01-01 AND' AND '{}-12-31' ORDER BY date ASC".format(start_year, end_year)
    self.cursor.execute(_SQL)
    for row in self.cursor.fetchall():
      self.list.append(row)

    return self.list

  def printData(self):
    """
      Created by: Chris Podolsky
      This function is used to tprint out all the data stored in the
      weather table. Used mostly for testing in this application.
    """

    self.conn = sqlite3.connect("weather.sqlite")
    self.cursor = self.conn.cursor()
    _SQL ="""select * from weather"""

    self.cursor.execute(_SQL)
    for row in self.cursor.fetchall():
      print(row)


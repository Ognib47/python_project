"""
  Data base operations class has data bas emethods for application.
"""
import sqlite3
class DBOperations():
  """
    Data base class for application.
  """

  def __init__(self):
    """
      Initialzies connection, cursor and variables
      used in the data base class.
    """

    self.conn = None
    self.cursor = None
    self.list = []

  def createTable(self):
    """
      This function creates a data base table for data
      to be insertersd into from the weather scraper class.
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
      This function accepts a dictionary of
      key values and inserts the data into the weather table.
    """

    for date, date_info in weather_data.items():
      self.cursor.execute("insert into weather(date, location, min_temp, max_temp, avg_temp)values (?,?,?,?,?)",
                          (date, "Winnipeg,MB", date_info['min_temp'], date_info['max_temp'], date_info['mean_temp']))
    self.conn.commit()
    self.conn.close()

  def plotData(self, start_year, end_year):
    """
      This function querries the data base for data based on user input
      Returns a cursor for all data between the given years.
    """

    self.conn = sqlite3.connect("weather.sqlite")
    self.cursor = self.conn.cursor()
    _SQL = "select date, avg_temp from weather where date BETWEEN '{}-01-01 AND' AND '{}-12-31'".format(start_year, end_year)
    self.cursor.execute(_SQL)
    for row in self.cursor.fetchall():
      self.list.append(row)

    return self.list

  def printData(self):
    """
      This function is used to tprint out all the data stored in the
      weather table. Used mostly for testing in this application.
    """

    self.conn = sqlite3.connect("weather.sqlite")
    self.cursor = self.conn.cursor()
    _SQL ="""select * from weather"""

    self.cursor.execute(_SQL)
    for row in self.cursor.fetchall():
      print(row)

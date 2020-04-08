import sqlite3

class DBOperations():

  def __init__(self):

    self.conn = None
    self.cursor = None

  def createTable(self):
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
    for date, date_info in weather_data.items():
      self.cursor.execute("insert into weather(date, location, min_temp, max_temp, avg_temp)values (?,?,?,?,?)",
                          (date, "Winnipeg,MB", date_info['min_temp'], date_info['max_temp'], date_info['mean_temp']))
    self.conn.commit()
    self.conn.close()


  def printData(self):
    self.conn = sqlite3.connect("weather.sqlite")
    self.cursor = self.conn.cursor()
    _SQL ="""select * from weather"""

    self.cursor.execute(_SQL)
    for row in self.cursor.fetchall():
      print(row)
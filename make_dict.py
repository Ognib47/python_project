from scrape_weather import MyHTMLParser
import urllib.request
from html.entities import name2codepoint
from datetime import datetime

myparser = MyHTMLParser()
today = datetime.today()
dict = {}

def make_dict():
  for year in range(1996, today.year + 1):
      for month in range(1, 13):
        with urllib.request.urlopen('https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&Year=' + str(year) + '&Month=' + str(month)) as response:
          res = str(response.read().decode())
          myparser.feed(res)
          myparser.data.popitem()
          dict = myparser.data
          # print(str(dict))
  return dict



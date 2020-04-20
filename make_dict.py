"""
  Created by: Chris Podolsky
  Function module to return a dictionary of dictionaries
  used to make the data base table. Works in conjunction
  with the scrape_weather class.
"""
from html.parser import HTMLParser
from scrape_weather import MyHTMLParser
import urllib.request
from html.entities import name2codepoint
from datetime import datetime

myparser = MyHTMLParser()
today = datetime.today()
data_dict = {}

def make_dict():
  """
    Created by: Chris Podolsky
    Function gets all available data from government weather
    website. Used in conjunction with the scrape_weather class.
    Uses a while loop to watch for matching titles and stop the loop.
    For loop goes backwards starting at december and goes to january.
  """
  year = today.year
  myparser.previous_title = "Start"

  while myparser.current_title != myparser.previous_title:
    for month in range(12, 0, -1):
      with urllib.request.urlopen('https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&Year=' + str(year) + '&Month=' + str(month)) as response:
        res = str(response.read().decode())
        myparser.feed(res)
    data_dict = myparser.data
    year -= 1
  return data_dict

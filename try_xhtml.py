from scrape_weather import MyHTMLParser
import urllib.request
from html.entities import name2codepoint


myparser = MyHTMLParser()

with urllib.request.urlopen('https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=2018&EndYear=2018&Day=1&Year=2018&Month=1') as response:
  res = str(response.read())

myparser.feed(res)




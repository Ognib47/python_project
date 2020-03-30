from html.parser import HTMLParser
import urllib.request
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.attr_value = ''
    self.nested_data = {}
    self.data = []
    self.inLink = False
    self.inTd = False
    self.inTr = False
    self.last_tag = None
    self.count = 0
    self.max_temp = None
    self.min_temp = None
    self.mean_temp = None
    self.dict_count = 1

  def handle_starttag(self, tag, attrs):
    if tag == 'tbody':
      self.inLink = True
    if tag == 'tr':
      self.inTr = True
    if tag == 'td':
      self.count += 1
      self.inTd = True
      self.last_tag = tag

  def handle_endtag(self, tag):
    if tag == 'tbody':
      self.inLink = False
    if tag == 'tr':
      self.inTr = False
      self.count = 0
    if tag == 'td':
      self.inTd = False



  def handle_data(self, data):
    if self.inLink and self.inTr and self.inTd and self.last_tag == 'td' and self.count <= 3 and data.strip():
      if self.count == 1:
        self.max_temp = data
      elif self.count == 2:
        self.min_temp = data
      elif self.count == 3:
        self.mean_temp = data
      if self.count == 3:
        self.nested_data.update({'max_temp': self.max_temp, 'min_temp': self.min_temp, 'mean_temp': self.mean_temp})
        self.data.append(self.nested_data)
        self.nested_data = {}

myparser = MyHTMLParser()
with urllib.request.urlopen('https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=2018&EndYear=2018&Day=1&Year=2018&Month=1') as response:
  res = str(response.read().decode())
  myparser.feed(res)
  myparser.data.pop(-1)
print(myparser.data)
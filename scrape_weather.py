from html.parser import HTMLParser
import urllib.request
from html.entities import name2codepoint
from datetime import datetime

class MyHTMLParser(HTMLParser):
  """
    Parser class used to scrape weather data from
    Governament of Canada weather page.
  """
  def __init__(self):
    """
      Initialize variables used to parse the data.
    """
    HTMLParser.__init__(self)
    self.attr_value = ''
    self.nested_data = {}
    self.data = {}
    self.inLink = False
    self.inTd = False
    self.inTr = False
    self.last_tag = None
    self.count = 0
    self.max_temp = None
    self.min_temp = None
    self.mean_temp = None
    self.dict_count = 1
    self.the_date = None
    self.inFormat = "%B %d, %Y"
    self.outFormat = "%Y-%m-%d"

  def handle_starttag(self, tag, attrs):
    """
      Detects the starting tags to look for the wanted
      data values.
    """
    if tag == 'tbody':
      self.inLink = True
    if tag == 'tr':
      self.inTr = True
    if tag == 'abbr' and self.inLink and self.inTr:
      for name, value in attrs:
        if name == 'title' and value != 'Average':
          self.the_date = value
    if tag == 'td':
      self.count += 1
      self.inTd = True
      self.last_tag = tag

  def handle_endtag(self, tag):
    """
      Detects end tags and shuts off the data.
    """
    if tag == 'tbody':
      self.inLink = False
    if tag == 'tr':
      self.inTr = False
      self.count = 0
    if tag == 'td':
      self.inTd = False

  def handle_data(self, data):
    """
      Creates a list of dictionaries containing the
      data to seed a database.

    """
    if self.inLink and self.inTr and self.inTd and self.last_tag == 'td' and self.count <= 3 and data.strip():
      if self.count == 1:
        self.max_temp = data
      elif self.count == 2:
        self.min_temp = data
      elif self.count == 3:
        self.mean_temp = data
      if self.count == 3:
        self.nested_data.update({'max_temp': self.max_temp, 'min_temp': self.min_temp, 'mean_temp': self.mean_temp})
        self.data.update({datetime.strptime(self.the_date, self.inFormat).strftime(self.outFormat): self.nested_data})
        self.nested_data = {}





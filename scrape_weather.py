"""
  Created by: Chris Podolsky
  Scrapes weather data from government weather website.
"""
from html.parser import HTMLParser
import urllib.request
from html.entities import name2codepoint
from datetime import datetime

class MyHTMLParser(HTMLParser):
  """
    Created by: Chris Podolsky
    Parser class used to scrape weather data from
    Governament of Canada weather page.
  """
  def __init__(self):
    """
      Created by: Chris Podolsky
      Initialize variables used to parse data.
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
    self.title = False
    self.head = False
    self.current_title = None
    self.previous_title = None

  def handle_starttag(self, tag, attrs):
    """
      Created by: Chris Podolsky
      Detects the starting tags to look for the wanted
      data values.Sets flag variables to true to control
      the data flow.
    """
    if tag == 'head':
      self.head = True
    if tag == 'title':
      self.title = True
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
      Created by: Chris Podolsky
      Detects end tags and sets flag variables to false
      this is used to control the data flow.
    """
    if tag == 'tbody':
      self.inLink = False
    if tag == 'tr':
      self.inTr = False
      self.count = 0
    if tag == 'td':
      self.inTd = False
    if tag == 'title':
      self.title = False
    if tag == 'head':
      self.head = False

  def handle_data(self, data):
    """
      Created by: Chris Podolsky
      Creates a list of dictionaries containing the
      data to seed a database.
    """
    if self.title and self.head and data.strip():
      self.previous_title = None
      self.previous_title = self.current_title
      self.current_title = None
      self.current_title = data
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

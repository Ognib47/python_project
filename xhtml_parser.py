from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.attr_value = ''
    self.colors = {}
    self.inLink = False
    self.last_tag = None

  def handle_starttag(self, tag, attrs):
    if tag == 'a':
      for name, value in attrs:
        if name == 'class' and value == 'tw':
          self.inLink = True
          self.last_tag = tag
        if name == 'href' and len(value) == 7:
          self.attr_value = value.replace('/', '#')

  def handle_endtag(self, tag):
    if tag == 'a':
      self.inLink = False

  def handle_data(self, data):
    if self.last_tag == 'a' and self.inLink and data.strip():
      self.colors.update({data: self.attr_value})

#!/usr/bin/env python

import os
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

template_path = os.path.join(os.path.dirname(__file__), 'templates')

class BaseHandler(webapp.RequestHandler):
  
  def __init__(self):
    self.data = {}

  def render(self, *path_components):
    self.response.out.write(template.render(os.path.join(template_path, *path_components), self.data))

def handler_for(template_name):
  class MainHandler(BaseHandler):
    def get(self):
      self.data.update(tab = template_name)
      self.render(template_name + '.html')
      
  return MainHandler

url_mapping = [
  ('/', handler_for('index')),
  ('/iphone/', handler_for('iphone')),
  ('/google-app-engine/', handler_for('google-app-engine')),
]

def main():
  application = webapp.WSGIApplication(url_mapping, debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()

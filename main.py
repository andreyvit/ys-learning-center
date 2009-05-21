#!/usr/bin/env python

import wsgiref.handlers
from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):

  def get(self):
    self.response.out.write('Hello world!')

url_mapping = [
  ('/', MainHandler),
]

def main():
  application = webapp.WSGIApplication(url_mapping, debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()

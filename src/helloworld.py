from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import ndb

import os

import jinja2
from cgi import log

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('Templates/testPage.html')
        self.response.write(
			template.render(
				{
					'name': 'joel',
				}
			)
		)

		
application = webapp.WSGIApplication(
	[
		('/', MainPage),
	], 
	debug=True,
)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

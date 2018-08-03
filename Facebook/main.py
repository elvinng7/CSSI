import webapp2
import jinja2
import os

from google.appengine.ext import ndb

env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Message(ndb.Model):
    content = ndb.StringProperty("content")
    created_time = ndb.DateTimeProperty(auto_now_add=True)


class Home(webapp2.RequestHandler):
    def get(self):
        messages = Message.query().order(-Message.created_time).fetch()
        templateVars = {
            'messages' : messages
        }
        template = env.get_template("templates/home.html")
        self.response.write(template.render(templateVars))

    def post(self):
        content = self.request.get('content')
        message = Message()
        message.content = content
        message.put()

app = webapp2.WSGIApplication([
    ("/", Home),
], debug=True)

import webapp2
import jinja2
import os
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

class Message(ndb.Model):
    name = ndb.StringProperty()
    content = ndb.StringProperty()
    create_time = ndb.DateTimeProperty(auto_now_add=True)

env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__))
)



class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info("this is the main app handler")

        login_url = ''
        logout_url = ''
        template = env.get_template('templates/guestbook.html')
       #The current user will be a user object or none
        current_user = users.get_current_user()

        #if no one is logged in. show ogin prompt.
        if not current_user:
            login_url = users.create_login_url('/')

        else:
            logout_url = users.create_logout_url('/')

        #read/write to the data base.
        message_query = Message.query()
        message_query = message_query.order(-Message.create_time)
        messages = message_query.fetch()


        templateVars = {
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'messages' : messages,
        }

        self.response.write(template.render(templateVars))

        def post(self):
            #1. get information from the request.
            content = self.request.get('content')
            email = current_user.email()
            #2 read/write to the database.
            message = Message(content=content, email=email)
            message.put()
            #3 render a response.
            self.redirect('/')

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)

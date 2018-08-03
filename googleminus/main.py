import webapp2
import jinja2
import os
import logging

#the handler section
from google.appengine.ext import ndb
from google.appengine.api import users


class Person(ndb.Model):    #schema for 
    name = ndb.StringProperty()
    biography = ndb.StringProperty()
    birthday = ndb.DateProperty()
    email = ndb.StringProperty()

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
        )

class CreateHandler(webapp2.RequestHandler):
    def post(self):
        name= self.request.get('name')
        biography= self.request.get('biography')
        current_user = users.get_current_user()
        email = current_user.email()

        person = Person(name=name, biography=biography, email=email)
        person.put()

        time.sleep(2)
        time.redirect('/')
class MainPage(webapp2.RequestHandler):
    def get(self): #for a GET request
        #1.) Read the Request.
        current_user = users.get_current_user()

        #2.) Read and write from database
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email()
            current_user = Person.query().filter(Person.email == current_email).get()
        else:
            current_user = None
        #3.) Render a response

        logout_url = users.create_logout_url('/')

        login_url = users.create_login_url('/')


        templateVars = {
            'people': people,
            'logout_url': logout_url,
            'login_url': login_url,
            'current_user': current_user,
        }
        template = env.get_template('templates/home.html')
        self.response.write(template.render(templateVars)) #the response

class ProfilePage(webapp2.RequestHandler):
    def get(self): #for a GET request
        #1 get information from the Request
        urlsafe_key = self.request.get('key')

        #2 read or write from
        key = ndb.Key(urlsafe=urlsafe_key)

        person = key.get()

        templateVars = {
            'person':person,
        } #x is the name of the object. person represents all the data in the object person.
        template = env.get_template('templates/profile.html')
        self.response.write(template.render(templateVars)) #the response


#the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),#this maps the root url to the MainPage Handler
    ('/profile', ProfilePage),
    ('/create', CreateHandler),
], debug=True)

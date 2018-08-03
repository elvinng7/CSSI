import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/home.html')
        self.response.write(template.render())

class SignUp(webapp2.RequestHandler):
    def post(self):
        templateVars = {
            'username': self.request.get('username'),

        }
        template = env.get_template('templates/signup.html')
        self.response.write(template.render(templateVars))
app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/signup", SignUp)

], debug=True)

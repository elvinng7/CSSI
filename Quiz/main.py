import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__))
)



class Quiz(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/quiz.html")
        self.response.write(template.render())

class Result(webapp2.RequestHandler):
    def POST(self):
        template = env.get_template("templates/results.html")
        templateVars = {
        "question1" : self.request.get("question1")
        "question2" : self.request.get("question2")
        "question3" : self.request.get("question3")

        }
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ("/", Quiz),
    ("/results", Result)

], debug=True)

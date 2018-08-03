import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class CollectInfo(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("template/collect_form.html")
        self.response.write(template.render())

class Story(webapp2.RequestHandler):
    def post(self):
        template = env.get_template("template/story.html")
        templateVars = {

        "protagonist" : self.request.get("protagonist"),
        "event" : self.request.get("event"),
        "pluralNoun" : self.request.get("pluralNoun"),
        "skill" : self.request.get("skill"),
        "name" : self.request.get("name"),
        "number" : self.request.get("number"),
        "largeNumber" : self.request.get("largeNumber"),
        "adjective" : self.request.get("adjective"),
        "place" : self.request.get("place"),
        }
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", CollectInfo),
    ("/story", Story),

], debug=True)

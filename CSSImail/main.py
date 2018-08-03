import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__))
)
class Email(object):
    def __init__ (self, subject, sender, content):
        self.subject = subject
        self.sender = sender
        self.content = content
emails = [
Email("Test1", "ciera@google.com", "This is a test email"),
Email("Test2", "ciera@google.com", "Second test"),
Email("Test3", "ciera@google.com", "Final test"),
]


class ListEmails(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/list_email.html")
        templateVars = {
            "emails" : emails
        }
        self.response.write(template.render(templateVars))



class ViewEmail(webapp2.RequestHandler):
    def get(self):
        subject = self.request.get("subject")
        sender = self.request.get("sender")
        content = self.request.get("content")
        template = env.get_template("templates/view_email.html")
        templateVars = {
            "subject" : subject,
            "sender" : sender,
            "content" : content,

        }
        self.response.write(template.render(templateVars))




app = webapp2.WSGIApplication([
    ("/", ListEmails),
    ("/viewemail", ViewEmail),

], debug=True)

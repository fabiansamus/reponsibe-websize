import webapp2
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t =jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class Art(db.Model):
	title=db.StringProperty(required=True)
	art=db.TextProperty(required=True)
	created=db.DateTimeProperty(auto_now_add=True)
		

class MainPage(Handler):
	def render_front(self, title="", art="", error=""):
		art= db.GqlQuery("")
		self.render("front.html",title=title,art=art,error=error)
	def get(self):
		self.render_front()
	def pos(self):
		title= self.request.get("title")
		art= self.request.get("art")

		if title and art:
			a=Art(title=get("title"))
			a.put()

			self.redirect("/")
		else:
			error = "we need both a title and some artwork!"
			self.render_front("front.html",title,art,error)
		
		

app = webapp2.WSGIApplication([('/', MainPage)],debug=True)
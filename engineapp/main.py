import webapp2
import cgi
import logging

form="""
<h2>Signup</h2>
<table>
    <form method="post">
    Username
    <label>
    <input type="text" name="username" value=""></label>
    <div style="color:red">%(error)s</div>
    <br>
    <label>
    Password
    <input type="password" name="password" value=""></label>
    <div style="color:red">%(errora)s</div>
    <br>
    <label>
    verify
    <input type="password" name="verify" value=""></label>
    <div style="color:red">%(errorb)s</div>
    <br>
    </table>
    <br>
    <input type="submit">
    </form>
"""
def rot13(new_text):
    lista=""
    for i in new_text:
            if "A"< i< "M":
                    lista +=chr(ord(i)+13)
            elif "N" <= i<="Z":
                    lista +=chr(ord(i)-13)
            elif "a" <= i<="m":
                    lista +=chr(ord(i)+13)
            elif "n" <= i<="z":
                    lista +=chr(ord(i)-13)
            else:
                    return False
    texto = cgi.escape(lista, quote=True)
    return  texto

class MainPage(webapp2.RequestHandler):
	def write_form(self, error="",errora="",errorb=""):
		self.response.out.write(form %{"error":error,
										"errora":errora,
										"errorb":errorb})

	def get(self):
		self.response.out.write()

	def post(self):
		username = self.request.get('username')
		password = self.request.get('password')
		verify = self.request.get('verify')
		if not rot13(username):
			self.write_form("is not a valid username","","")
		elif len(password)< 3 or password != verify:
			if len(password)< 3:
				self.write_form("","is not a valid password","")
			elif password != verify:
				self.write_form("","","password didn't match")
		else:
			self.redirect("/thanks",username)
class ThanksHandler(webapp2.RequestHandler):
	def get(self, name):
		self.response.out.write("Thanks for log in %s"% name)
			



app = webapp2.WSGIApplication([('/', MainPage),('/thanks',ThanksHandler)],debug=True)
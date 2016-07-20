import webapp2
import cgi
import logging

form="""
<form method="post">
	Enter some text to ROT13
	<br>
	<label>
	<textarea name="text" style="height: 100px; width:400px;">%(text)s</textarea>
	</label>
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
                    lista +=i
    texto = cgi.escape(lista, quote=True)
    return  texto

class MainPage(webapp2.RequestHandler):
	def write_form(self, text=""):
		self.response.out.write(form % {"text":text})

	def get(self):
		self.write_form()

	def post(self):
		new_text = self.request.get('text')
		text= rot13(new_text)
		self.write_form(text)

	

	

		


app = webapp2.WSGIApplication([('/', MainPage)],debug=True)


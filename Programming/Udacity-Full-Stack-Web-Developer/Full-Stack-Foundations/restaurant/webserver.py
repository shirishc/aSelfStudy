from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, RestaurantDB, MenuItemDB

engine = create_engine('postgresql:///restaurantmenu')
DBSession = sessionmaker(bind = engine)
session = DBSession()

class WebServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				output = ""
				output += "<html><body>Hello!"
				output += """<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>What would you like to say?</h2><input name='message' type='text'><input type='submit' value ='Submit'></form>"""
				output += "</html></body>"
				self.wfile.write(output)
				print output
				return

			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				output = ""
				output += "<html><body> &#161 Hola! <a href = '/hello'>Back to Hello</a>"
				output += """<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>What would you like to say?</h2><input name='message' type='text'><input type='submit' value ='Submit'></form>"""
				output += "</html></body>"
				self.wfile.write(output)
				return

			if self.path.endswith("/restaurants"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				restaurants = session.query(RestaurantDB).all()

				output = ""
				output += "<br><br><a href = '/restaurants/new'>Insert a new restaurant</a><br>"
				output += "<html><body><h1>List of Restaurants</h1>"
				
				for aRest in restaurants:
					output += aRest.name
					output += "<br><a href = '/restaurants/%s/edit'>Edit</a>" % aRest.id
					output += "<br><a href = '/restaurants/%s/delete'>Delete</a>" % aRest.id
					output += "<br><br>"

				output += "</html></body>"
				self.wfile.write(output)
				return

			if self.path.endswith("/restaurants/new"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				output = "<html><body>"
				output += "<h1>Make a New Restaurant</h1>"
				output += """<form method = 'POST' enctype='multipart/form-data' action='/restaurants/new'><h2>Enter the name of the new restaurant</h2><input name='newRestName' type='text'><input type='submit' value ='Create'></form>"""
				output += "</html></body>"
				self.wfile.write(output)
				return

			if self.path.endswith("/edit"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				restId = self.path.split("/")[-2]
				aRest = session.query(RestaurantDB).filter_by(id=int(restId)).one()
				if aRest != []:
					output = ""
					output += "<html><body>"
					output += "<h1>Edit the Restaurant - %s</h1>" % aRest.name
					output += "<form method = 'POST' enctype='multipart/form-data' action='%s'><h2>Change the details</h2>" % self.path
					output += "<input name='updRestName' type='text' placeholder=%s>" % aRest.name
					output += "<input type='submit' value ='Update'></form>"
					output += "</html></body>"
					self.wfile.write(output)
					return

			if self.path.endswith("/delete"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				restId = self.path.split("/")[-2]
				aRest = session.query(RestaurantDB).filter_by(id=int(restId)).one()
				if aRest != []:
					output = ""
					output += "<html><body>"
					output += "<h1>Delete the Restaurant - %s ?</h1>" % aRest.name
					output += "<form method = 'POST' enctype='multipart/form-data' action='%s'><h2>Delete ?</h2>" % self.path
					output += "<input type='submit' value ='Delete'></form>"
					output += "</html></body>"
					self.wfile.write(output)
					return
		except IOError:
			self.send_error(404, "File Not Found %s" % self.path)

	def do_POST(self):
		try:
			
			if self.path.endswith(("/hello", "/hola" )):
				self.send_response(301)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)

				messagecontent = fields.get('message')

				output = ""
				output += "<html><body>"
				output += "<h2> Okay, how about this: </h2>"
				output += "<h1> %s </h1>" % messagecontent[0]
				output += """<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>What would you like to say?</h2><input name='message' type='text'><input type='submit' value ='Submit'></form>"""
				output += "</html></body>"
				self.wfile.write(output)
				return

			if self.path.endswith("/restaurants/new" ):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)

				restName = fields.get('newRestName')
				newRestaurant = RestaurantDB(name = restName[0])
				session.add(newRestaurant)
				session.commit()

				self.send_response(301)
				self.send_header("Content-type", "text/html")
				self.send_header("Location", "/restaurants")
				self.end_headers()

			if self.path.endswith("edit" ):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)

				restId = self.path.split("/")[-2]
				aRest = session.query(RestaurantDB).filter_by(id=int(restId)).one()

				if aRest != []:
					restName = fields.get('updRestName')
					aRest.name = restName[0]
					session.add(aRest)
					session.commit()
					self.send_response(301)
					self.send_header("Content-type", "text/html")
					self.send_header("Location", "/restaurants")
					self.end_headers()

			if self.path.endswith("delete"):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)

				restId = self.path.split("/")[-2]
				aRest = session.query(RestaurantDB).filter_by(id=int(restId)).one()

				if aRest != []:
					session.delete(aRest)
					session.commit()
					self.send_response(301)
					self.send_header("Content-type", "text/html")
					self.send_header("Location", "/restaurants")
					self.end_headers()

		except:
			pass

			
def main():
	try:
		port = 8080
		server = HTTPServer(('', port), WebServerHandler)
		print "Webserver listening on port - %s" % port
		server.serve_forever()

	except KeyboardInterrupt:
		print "^C entered, Stopping web server"
		server.socket.close()

if __name__ == "__main__":
	main()

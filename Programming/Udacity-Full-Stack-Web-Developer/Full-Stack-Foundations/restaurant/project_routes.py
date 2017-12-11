from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, RestaurantDB, MenuItemDB

engine = create_engine('postgresql:///restaurantmenu')
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
	output = ""
	aRest = session.query(RestaurantDB).filter_by(id = restaurant_id).one()
	items = session.query(MenuItemDB).filter_by(restaurant_id = aRest.id)
	for anItem in items:
		output += anItem.name + "<br>" + anItem.price + "<br>" + \
					anItem.description + "<br><br>"
	return output
	
@app.route('/restaurants/<int:restaurant_id>/new')
def newMenuItem(restaurant_id):
	return "page to create new Menu item"

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
	return "page to edit Menu item"

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
	return "page to delete Menu item"

if __name__ == '__main__':
	app.debug = True
	app.run(host = "0.0.0.0", port = 5000)
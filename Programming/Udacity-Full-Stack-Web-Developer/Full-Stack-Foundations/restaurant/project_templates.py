from flask import Flask, render_template, url_for, request, redirect
from flask import flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, RestaurantDB, MenuItemDB

engine = create_engine('postgresql:///restaurantmenu')
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/')
def restaurantList():
	restList = session.query(RestaurantDB).all()
	return render_template("restaurants.html", restaurants = restList)

@app.route('/restaurants/new', methods=['GET', 'POST'])
def newRestaurant():
	if request.method == 'POST':
		newRest = RestaurantDB(name = request.form['name'])
		session.add(newRest)
		session.commit()
		flash("new restaurant created !!!")
		return redirect(url_for('restaurantList'))
	else:
		return render_template('newRestaurant.html')

@app.route('/restaurants/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
	restToEdit = session.query(RestaurantDB).filter_by(id=restaurant_id).one()
	if request.method == 'POST':
		restToEdit.name = request.form['name']
		session.add(restToEdit)
		session.commit()
		flash("Restaurant edited !!!")
		return redirect(url_for('restaurantList'))
	else:
		return render_template('editRestaurant.html', restaurant=restToEdit)

@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
	restToDel = session.query(RestaurantDB).filter_by(id=restaurant_id).one()
	if request.method == 'POST':
		session.delete(restToDel)
		session.commit()
		flash("Restaurant deleted !!!")
		return redirect(url_for('restaurantList'))
	else:
		return render_template('deleteRestaurant.html', restaurant=restToDel)

@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
	aRest = session.query(RestaurantDB).filter_by(id = restaurant_id).one()
	items = session.query(MenuItemDB).filter_by(restaurant_id = aRest.id)
	return render_template("menu.html", restaurant = aRest, items = items)
	
@app.route('/restaurants/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
	if request.method == 'POST':
		newMenuItem = MenuItemDB(name = request.form['name'], restaurant_id = restaurant_id)
		session.add(newMenuItem)
		session.commit()
		flash("new menu item created !!!")
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		return render_template('newMenuItem.html', restaurant_id = restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
	itemToEdit = session.query(MenuItemDB).filter_by(id=menu_id).one()
	if request.method == 'POST':
		itemToEdit.name = request.form['name']
		session.add(itemToEdit)
		session.commit()
		flash("menu item edited !!!")
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
		return render_template('editMenuItem.html', restaurant_id = restaurant_id, menuitem=itemToEdit)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
	itemToDelete = session.query(MenuItemDB).filter_by(id=menu_id).one()
	if request.method == 'POST':
		session.delete(itemToDelete)
		session.commit()
		flash("menu item deleted !!!")
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
		return render_template('deleteMenuItem.html', restaurant_id = restaurant_id, menuitem=itemToDelete)

@app.route('/restaurants/JSON')
def restaurantsJSON():
	items = session.query(RestaurantDB).all()
	return jsonify(Restaurants=[item.serialize for item in items])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
	aRest = session.query(RestaurantDB).filter_by(id = restaurant_id).one()
	items = session.query(MenuItemDB).filter_by(restaurant_id = aRest.id)
	return jsonify(MenuItems=[item.serialize for item in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
	item = session.query(MenuItemDB).filter_by(id = menu_id).one()
	return jsonify(MenuItem=item.serialize)

if __name__ == '__main__':
	app.secret_key = "super_secret_key"
	app.debug = True
	app.run(host = "0.0.0.0", port = 5000)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, RestaurantDB, MenuItemDB

engine = create_engine('postgresql:///restaurantmenu')
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Add a new resturant to the database
myFirstRestaurant = RestaurantDB(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

# Read the database using query
rows = session.query(RestaurantDB).all()

# Add a new MenuItem to the database
cheesePizza = MenuItemDB(name = "Cheese Pizza",
						description = "Made with all fresh ingredients",
						price = "$8.99", course = "Entree", 
						restaurant = myFirstRestaurant)
session.add(cheesePizza)
session.commit()

# Read the database using query
rows = session.query(MenuItemDB).all()

veggieBurgers = session.query(MenuItemDB).filter_by(name = "Veggie Burger")
for veggieBurger in veggieBurgers:
	print veggieBurger.id
	print veggieBurger.price
	print veggieBurger.restaurant.name
	print "\n"

# For updating the database with price changes
UrbanVeggieBurger = session.query(MenuItemDB).filter_by(id=8).one()
UrbanVeggieBurger.price = "$2.99"
session.add(UrbanVeggieBurger)
session.commit()

# For deleting a menu item fromt he database
spinach = session.query(MenuItemDB).filter_by(name = "Spinach Ice Cream").one()
session.delete(spinach)
session.commit()

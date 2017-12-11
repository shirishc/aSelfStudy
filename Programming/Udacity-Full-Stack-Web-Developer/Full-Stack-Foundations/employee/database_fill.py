from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, EmployeeDB, AddressDB

engine = create_engine('postgresql:///employeedb')
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Add a new Employee to the database
newEmployee = EmployeeDB(name = "Rebecca Allen")
session.add(newEmployee)
session.commit()

# Read the database using query
session.query(EmployeeDB).all()

# Add a new address to the database
rebeccaAddress = AddressDB(street = "512 Sycamore Road", 
							zip = "02001",
							employee = newEmployee)
session.add(rebeccaAddress)
session.commit()

# Read the database using query
session.query(AddressDB).all()

# For updating the database with price changes
rebecca = session.query(EmployeeDB).filter_by(name = "Rebecca Allen").one()
rebeccaAdd = session.query(AddressDB).filter_by(employee_id = rebecca.id).one()

rebeccaAdd.street = "281 Summer Circle"
rebeccaAdd.zip = "00819"
session.add(rebeccaAdd)
session.commit()

# For deleting employee from the database
mark = session.query(EmployeeDB).filter_by(name = "Mark Gonzalez").one()
session.delete(mark)
session.commit()

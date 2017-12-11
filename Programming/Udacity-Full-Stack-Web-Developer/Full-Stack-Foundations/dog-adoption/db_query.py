from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy, PuppyEx
from datetime import date
from dateutil.relativedelta import relativedelta

engine = create_engine('postgresql:///puppyshelterdb')
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Read the database using query
session.query(Shelter).all()

# Read the database using query
puppies = session.query(Puppy).order_by(Puppy.name).all()
for aPuppy in puppies:
	print aPuppy.name, aPuppy.dateOfBirth, aPuppy.weight

dtReq = date.today() + relativedelta(months = -6) 
puppies = session.query(Puppy).filter(Puppy.dateOfBirth > dtReq).order_by(Puppy.dateOfBirth).all()
for aPuppy in puppies:
	print aPuppy.name, aPuppy.dateOfBirth, aPuppy.weight

puppyGrp = session.query(Puppy).order_by(Puppy.shelter_id).all()
for aPuppy in puppyGrp:
	print aPuppy.name, aPuppy.dateOfBirth, aPuppy.shelter.name

# For updating the database with price changes
# rebecca = session.query(ShelterDB).filter_by(name = "Rebecca Allen").one()
# rebeccaAdd = session.query(PuppyDB).filter_by(employee_id = rebecca.id).one()

# rebeccaAdd.street = "281 Summer Circle"
# rebeccaAdd.zip = "00819"
# session.add(rebeccaAdd)
# session.commit()

# For deleting employee from the database
# mark = session.query(ShelterDB).filter_by(name = "Mark Gonzalez").one()
# session.delete(mark)
# session.commit()

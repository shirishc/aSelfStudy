from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Shelter, Puppy, PuppyEx, Adopter
from datetime import date
from dateutil.relativedelta import relativedelta

engine = create_engine('postgresql:///puppyshelterdb')
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Function to look for an empty shelter for the puppy
def FindShelter(cityName):
	allShelters = session.query(Shelter).filter(
					Shelter.city == cityName, 
					Shelter.current_occupancy < Shelter.maximum_capacity).all()
	availShelters = []
	for aShelter in allShelters:
		availShelters.append((aShelter.name, aShelter.address, aShelter.city))

	return availShelters

def AdoptPuppies(puppyIDs, adopterIDs):
	for puppyID in puppyIDs:
		aPuppy = session.query(Puppy).filter(Puppy.id == puppyID).one()
		for adopterID in adopterIDs:
			anAdopter = session.query(Adopter).filter(Adopter.id == adopterID).one()
			aPuppy.adopters.append(anAdopter)
		aPuppy.shelter.current_occupancy -= 1
	session.commit()


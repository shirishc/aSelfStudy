import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Table

Base = declarative_base()

class Gender(enum.Enum):
	male = "male"
	female = "female"

class Shelter(Base):
	__tablename__ = 'shelter'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	address = Column(String(250), )
	city = Column(String(100))
	state = Column(String(25))
	zipCode = Column(String(5))
	website = Column(String(250))
	current_occupancy = Column(Integer)
	maximum_capacity = Column(Integer)

puppy_adopter = Table("puppy_adopter", Base.metadata,
			Column("puppy_id", ForeignKey("puppy.id"), primary_key = True),
			Column("adopter_id", ForeignKey("adopter.id"), primary_key = True))

class Puppy(Base):
	__tablename__ = 'puppy'

	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	gender = Column(String(8), nullable=False)
	dateOfBirth = Column(Date)
	picture = Column(String)
	weight = Column(Numeric)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	puppy_ex = relationship("PuppyEx", uselist=False, back_populates = "puppy")
	adopters = relationship("Adopter", secondary = puppy_adopter, 
							back_populates = "puppies")
	

class PuppyEx(Base):
	__tablename__ = 'puppies_ex'

	puppy_id = Column(Integer, ForeignKey("puppy.id"), primary_key = True)
	photo_url = Column(String)
	description = Column(String)
	special_needs = Column(String)
	puppy = relationship(Puppy, back_populates = "puppy_ex")


class Adopter(Base):
	__tablename__ = "adopter"

	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	puppies = relationship(Puppy, secondary = puppy_adopter, 
							back_populates = "adopters")

engine = create_engine('postgresql:///puppyshelterdb')
Base.metadata.create_all(engine)


import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class EmployeeDB(Base):
	__tablename__ = 'employee'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

class AddressDB(Base):
	__tablename__ = 'address'
	street = Column(String(80))
	zip = Column(String(5))
	id = Column(Integer, primary_key=True)
	employee_id = Column(Integer, ForeignKey('employee.id'))
	employee = relationship(EmployeeDB)

engine = create_engine('postgresql:///employeedb')
Base.metadata.create_all(engine)


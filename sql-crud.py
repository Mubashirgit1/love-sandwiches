from sqlalchemy import (create_engine, Column, Float, ForeignKey, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instruction to create a connection to the database chinook
db = create_engine("postgresql+psycopg2://postgres:mubashir@localhost:5432/chinook")
Base = declarative_base()

# create class based model for artist table
class Artist(Base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)
# create class based model for album table
class Album(Base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))

# create class based model for track table
class Track(Base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer)
    bytes = Column(Integer)
    unit_price = Column(Float)

# create a class based model for programmer table
class Programmer(Base):
    __tablename__ = "Programmer"
    programmer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    Nationality = Column(String)
    famous_for = Column(String)

# instead of creating table variable we create class we wil ask for session 
# create  a new instance of sessionmaker
Session = sessionmaker(db)
session = Session()    
# create the database using declarative_base subclass
Base.metadata.create_all(db)

# create a new programmer record
new_programmer = Programmer(
    first_name = "Mudasser",
    last_name = "hussain",
    gender = "Male",
    Nationality = "Pakistan",
    famous_for = "manager")
# session.add(new_programmer)
# session.commit()

# update a record programmer
# programmer = session.query(Programmer).filter_by(programmer_id=1).first()
# programmer.famous_for = "Python Developer"
# session.commit()

# update multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.Nationality == "Pakistan":
#         person.Nationality = "british"
# session.commit()

# # delete a record
# fname = input("Enter the first name of the programmer you want to delete: ")
# lname = input("Enter the last name of the programmer you want to delete: ")
# programmer = session.query(Programmer).filter_by(first_name=fname,last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer Found: ",programmer.first_name,programmer.last_name)
#     confirm = input("Are you sure you want to delete this record? (y/n): ")
#     if confirm.lower() == 'y':
#         session.delete(programmer)
#         session.commit()
#         print("Record deleted successfully")
#     else:
#         print("Record not deleted")
# else:        
#     print("No record found")

# delete all records
programmers = session.query(Programmer)
for Programmer in programmers:
    session.delete(Programmer)
    session.commit()

#  querying the database
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.programmer_id,
        programmer.first_name,
        programmer.last_name,
        programmer.gender,
        programmer.Nationality,
        programmer.famous_for,)  
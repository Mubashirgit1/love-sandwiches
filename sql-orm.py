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


# instead of creating table variable we create class we wil ask for session 
# create  a new instance of sessionmaker
Session = sessionmaker(db)
session = Session()    
# create the database using declarative_base subclass
Base.metadata.create_all(db)

# querying the database 
# query 1 selct all records in artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.artist_id, artist.name,sep="|")

# query 2 select name column in artist table
# artists = session.query(Artist)  
# for artist in artists:
#     print(artist.name)    
# query 3 select records in artist table where name is queen
# artist = session.query(Artist).filter_by(name = "Queen").first()
# print(artist.artist_id, artist.name, sep=" | ")
# query 4 select records in artist table where artist_id is 51
# artist = session.query(Artist).filter_by(artist_id = 51).first()
# print(artist.artist_id, artist.name, sep=" | ")
# query 5 select records in artist table where name is queen
# artists = session.query(Album).filter_by(artist_id = 51)
# for artist in artists:            
#     print(artist.artist_id, artist.name, sep=" | ")
# query 6 select records in track table where composer is queen
tracks = session.query(Track).filter_by(composer = "Queen")
for track in tracks:
    print(track.track_id, track.name, track.composer, sep=" | ")
# close the session


from app import app, db

#the User model: each user has a username, and a playlist_id foreign key referring
#to the user's Playlist
class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), index = True, unique = True) 
  playlist_id = db.Column(db.Integer,  db.ForeignKey('playlist.id'))
  
  #representation method
  def __repr__(self):
        return "{}".format(self.username)

#create the Song model here + add a nice representation method)
class Song(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  artist = db.Column(db.String(50), index = True, unique = False)
  title = db.Column(db.String(60), index = True, unique = False)
  n = db.Column(db.Integer, index = False, unique = False)
   
  def __repr__(self):
    return "{} by {}".format(self.artist, self.title)

#create the Item model here + add a nice representation method
# Playlist and Item are one-to-many model
class Item(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  
  song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
#create the Playlist model here + add a nice representation method
  playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))

class Playlist(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
  #foreign_key = db.Column(db.Integer, db.ForeignKey('playlist_id'))
  items = db.relationship('Item', backref='playlist', lazy='dynamic')


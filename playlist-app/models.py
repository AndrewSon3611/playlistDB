"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlist'

    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    songs = db.relationship('Song', secondary='playlist_song', back_populates='playlists')

class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'

    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    artist = db.Column(db.String(255))
    playlists = db.relationship('Playlist', secondary='playlist_song', back_populates='songs')

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlist_songs'

    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

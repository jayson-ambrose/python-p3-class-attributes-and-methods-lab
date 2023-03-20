import ipdb

class Song:
    
    count = 0
    artists = []
    genres = []       
    genre_count = {}       #class attributes
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist  #instance attributes
        self.genre = genre

        #class methods firing on instantiation of new class object.
        Song.count += 1 
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod  #this is a class method believe it or not.
    def add_to_genres(cls, genre):

        if genre in cls.genres:
            return
        else:
            print("new genre added")
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):

        if artist in cls.artists:
            return
        else:
            print("new artist added")
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre): 
        if genre in cls.genre_count.keys():
            cls.genre_count[genre] +=1
        else:
            cls.genre_count[genre] = 1 

    @classmethod
    def add_to_artist_count(cls, artist): 
        if artist in cls.artist_count.keys():
            cls.artist_count[artist] +=1
        else:
            cls.artist_count[artist] = 1     

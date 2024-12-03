# GLORY BE TO GOD,
# PYTHON PROGRAMMING - PYTHON - CLASS ATTRIBUTES AND METHODS
# BY ISRAEL MAFABI EMMANUEL

class Song:
    # Class scope - Global scope
    # Global Variables
    count:int = 0
    genre_count:dict  = {}
    artist_count:dict = {}

    genres:list  = []
    artists:list = []

    def __init__(self, name:str, artist:str, genre:str):
        self.name   = name
        self.artist = artist
        self.genre  = genregit
        Song.add_song_to_count()
        Song.add_to_artists(artist)
        Song.add_song_to_genre(genre)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls, _artist_):
        if _artist_ not in cls.artists:
            # we add to the list
            cls.artists.append(_artist_)
        else:
            print("Artist already recorded...")

    @classmethod
    def add_song_to_genre(cls, _genre_):
        if _genre_ not in cls.genres:
            # we add to the list
            cls.genres.append(_genre_)
        else:
            print("Song is alread in the Genre!")

    @classmethod
    def add_to_genre_count(cls, _genre_):
        # song is present in the genre list
        if _genre_ in cls.genre_count:
            # we increment by one...
            cls.genre_count[_genre_] += 1
        else:
            cls.genre_count[_genre_] = 1


    @classmethod
    def add_to_artist_count(cls, _artist_):
        # song is present in the genre list
        if _artist_ in cls.artist_count:
            # we increment by one...
            cls.artist_count[_artist_] += 1
        else:
            cls.artist_count[_artist_] = 1

    @classmethod
    def print_songs(cls):
        print(f"Genre Count: {cls.genre_count}")
        print(f"Genre List : {cls.genres}")
        print(f"Artist List: {cls.artists}")

song_1 = Song("This is the Life", "Amy", "Rock")
Song.print_songs()
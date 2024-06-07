class Song:
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count= {}
    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.name = name
        self.artist = artist
        self.genre = genre
    @classmethod
    def add_to_genres(self, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)
    @classmethod
    def add_to_artists(self, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 1
        else: 
            Song.genre_count[genre] += 1
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, new_genre):
        self._genre = new_genre
        Song.add_to_genres(new_genre)
        Song.add_to_genre_count(new_genre)
    @property
    def artist(self):
        return self._artist
    @artist.setter
    def artist(self, new_artist):
        self._artist = new_artist
        Song.add_to_artists(new_artist)
        Song.add_to_artist_count(new_artist)
        
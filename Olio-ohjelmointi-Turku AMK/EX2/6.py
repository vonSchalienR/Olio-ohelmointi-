class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"Book: {self.name}, Author: {self.author}, Genre: {self.genre}, Year: {self.year}"


class Manga:
    def __init__(self, name, writer, genre, year):
        self.name = name
        self.writer = writer
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"Manga: {self.name}, Writer: {self.writer}, Genre: {self.genre}, Year: {self.year}"


class Anime:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"Anime: {self.name}, Director: {self.director}, Genre: {self.genre}, Year: {self.year}"


class Movie:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"Movie: {self.name}, Director: {self.director}, Genre: {self.genre}, Year: {self.year}"


class Song:
    def __init__(self, name, artist, genre, year):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"Song: {self.name}, Artist: {self.artist}, Genre: {self.genre}, Year: {self.year}"


# Example usage:
book = Book("1984", "George Orwell", "Dystopian", 1949)
manga = Manga("One Piece", "Eiichiro Oda", "Adventure", 1997)
anime = Anime("Attack on Titan", "Tetsurō Araki", "Action", 2013)
movie = Movie("Inception", "Christopher Nolan", "Sci-Fi", 2010)
song = Song("Bohemian Rhapsody", "Queen", "Rock", 1975)

print(book)
print(manga)
print(anime)
print(movie)
print(song)

import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository

album_repository.delete_all_albums()
artist_repository.delete_all_artists()

artist_1 = Artist("Louf")
artist_repository.save(artist_1)
artist_2 = Artist("Toro Y Moi")
artist_repository.save(artist_2)

album_1 = Album("Our Intervals", artist_1, "Electronic")
album_repository.save(album_1)
album_2 = Album("Outer Peace", artist_2, "Alternative Pop")
album_repository.save(album_2)
album_3 = Album("Boo Boo", artist_2, "Alternative Pop")
album_repository.save(album_3)

albums = album_repository.select_all_albums()
for album in albums:
    print(album.__dict__)


